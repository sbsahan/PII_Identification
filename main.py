from presidio_analyzer import AnalyzerEngine, LemmaContextAwareEnhancer
from presidio_anonymizer import AnonymizerEngine
import config

from groq import Groq

from identifiers.BT_Identifier import BTRecognizer
from identifiers.MAC_Identifier import MACRecognizer
from identifiers.Medication_Identifier import MedicationRecognizer
from identifiers.TCKN_Identifier import TCKNRecognizer  
from commands import get_commands

client = Groq(
    api_key=config.groqConf.api_key,
)

selectedModel = "llama-3.3-70b-versatile"
models = client.models.list()
indexed_models = [f"[{i}] {model.id}" for i, model in enumerate(models.data)]


medication_recognizer = MedicationRecognizer()
blood_type_recognizer = BTRecognizer()
mac_address_recognizer = MACRecognizer()
tckn_recognizer = TCKNRecognizer()

analyzer = AnalyzerEngine(context_aware_enhancer=LemmaContextAwareEnhancer(context_suffix_count=5), supported_languages=["en"])

analyzer.registry.add_recognizer(tckn_recognizer)
analyzer.registry.add_recognizer(medication_recognizer)
analyzer.registry.add_recognizer(blood_type_recognizer)
analyzer.registry.add_recognizer(mac_address_recognizer)


anonymizer = AnonymizerEngine()

print("You are now chatting with", selectedModel, "!")

messagesSent = []
selectedModel_ref = [selectedModel]  # Use a mutable reference for selectedModel


while True:
    text = input()
    if text.startswith("!"):
        command = text.lower()
        commands = get_commands()
        action = commands.get(command, None)
        if action:
            if command == "!clear":
                action(messagesSent)
            elif command == "!models":
                action(indexed_models, models, selectedModel_ref)
                selectedModel = selectedModel_ref[0]
            else:
                result = action()
                if result == 'break':
                    break
        else:
            print("Unknown command. Type !help for a list of commands.")
        continue
    
    analyzer_results = analyzer.analyze(text=text, language="en", score_threshold=0.2)
    print(analyzer_results)
    anonymizer_results = anonymizer.anonymize(text=text, analyzer_results=analyzer_results)

    if anonymizer_results.text != text:
        print("PII identified, your message has been anonymized to: ", anonymizer_results.text)
        print("Wrongly identified PII? Type 'y' to send the original message,'n' to send the anonymized message or 'c' to cancel sending the message.")
        
        textoverride = input().lower()
        inputGiven = False
        
        while not inputGiven:
            if textoverride == "y":
                messagesSent.append({
                    "role": "user",
                    "content": text
                })
                inputGiven = True
            elif textoverride == "n":
                messagesSent.append({
                    "role": "user",
                    "content": anonymizer_results.text
                })
                inputGiven = True
            elif textoverride == "c":
                print("Message sending cancelled.")
                inputGiven = True
            else:
                print("Invalid input. Please type 'y' to send the original message or 'n' to send the anonymized message.")
                textoverride = input().lower()
    else:
        messagesSent.append({
            "role": "user",
            "content": anonymizer_results.text
        })

    a = client.chat.completions.create(
        messages=messagesSent,
        model=selectedModel,
    )

    print(a.choices[0].message.content)