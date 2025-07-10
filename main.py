from presidio_analyzer import AnalyzerEngine, LemmaContextAwareEnhancer
from presidio_anonymizer import AnonymizerEngine
from colorama import Fore, Style, init
import config

from groq import Groq

from identifiers.BT_Identifier import BTRecognizer
from identifiers.MAC_Identifier import MACRecognizer
from identifiers.Medication_Identifier import MedicationRecognizer
from identifiers.TCKN_Identifier import TCKNRecognizer  
from commands import get_commands
import style_utils as su

init(autoreset=True)

client = Groq(
    api_key=config.groqConf.api_key,
)

selectedModel = "compound-beta"
model_ids = [
    "deepseek-r1-distill-llama-70b",
    "gemma2-9b-it",
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile",
    "meta-llama/llama-4-maverick-17b-128e-instruct",
    "qwen/qwen3-32b",
    "compound-beta",
    "compound-beta-mini"
]

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

print(su.dim("You are now chatting with"), 
      su.cyan(selectedModel), 
      su.dim("!"))

messagesSent = []
selectedModel_ref = [selectedModel]  # Use a mutable reference for selectedModel


while True:
    text = input(su.user_label() + " ")
    if text.startswith("!"):
        command = text.lower()
        commands = get_commands()
        action = commands.get(command, None)
        if action:
            if command == "!clear":
                action(messagesSent)
            elif command == "!models":
                action(model_ids, selectedModel_ref, messagesSent)
                selectedModel = selectedModel_ref[0]
            else:
                result = action()
                if result == 'break':
                    break
        else:
            print(su.dim("Unknown command. Type"), 
                  su.cyan("!help"), 
                  su.dim("for a list of commands."))
        continue
    
    analyzer_results = analyzer.analyze(text=text, language="en", score_threshold=0.2)
    print(analyzer_results)
    anonymizer_results = anonymizer.anonymize(text=text, analyzer_results=analyzer_results)

    if anonymizer_results.text != text:
        print(su.dim("PII identified, your message has been anonymized to:"), 
              su.yellow(anonymizer_results.text)
        )
        print(su.dim("Wrongly identified PII? Type"), 
              su.green('\"y\"'), 
              su.dim("to send the original message,"), 
              su.magenta('\"n\"'), 
              su.dim("to send the anonymized message or"), 
              su.red('\"c\"'), 
              su.dim("to cancel sending the message.")
        )
        
        textoverride = input(su.user_label() + " ").lower()
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
                print(su.dim("Message sending cancelled."))
                inputGiven = True
            else:
                print(su.dim("Invalid input. Please type"), 
                      su.green('\"y\"'), 
                      su.dim("to send the original message or"), 
                      su.magenta('\"n\"'), 
                      su.dim("to send the anonymized message."))
                textoverride = input(su.user_label() + " ").lower()
    else:
        messagesSent.append({
            "role": "user",
            "content": anonymizer_results.text
        })

    if len(messagesSent) > 0:
        a = client.chat.completions.create(
            messages=messagesSent,
            model=selectedModel,
        )

        print(su.assistant_label(), a.choices[0].message.content)