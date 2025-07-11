from time import sleep
from presidio_analyzer import AnalyzerEngine, LemmaContextAwareEnhancer
from presidio_anonymizer import AnonymizerEngine
from colorama import init
import config

from groq import Groq

from identifiers.BT_Identifier import BTRecognizer
from identifiers.MAC_Identifier import MACRecognizer
from identifiers.Medication_Identifier import MedicationRecognizer
from identifiers.TCKN_Identifier import TCKNRecognizer  
from commands import get_commands
import utils

init(autoreset=True)

client = Groq(
    api_key=config.groqConf.api_key,
)

selectedModel = config.groqConf.selectedModel
model_ids = config.groqConf.model_ids

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

utils.outputText.chattingWith()

messagesSent = []
selectedModel_ref = [selectedModel]  # Use a mutable reference for selectedModel


while True:
    text = input(utils.user_label() + " ")
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
            utils.outputText.unknownCommand()
        continue
    
    analyzer_results = analyzer.analyze(text=text, language="en", score_threshold=0.2)
    anonymizer_results = anonymizer.anonymize(text=text, analyzer_results=analyzer_results)
    

    if anonymizer_results.text != text:
        utils.outputText.messageAnonymized(anonymizer_results.text)
        
        textoverride = input(utils.user_label() + " ").lower()
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
                utils.outputText.messageCancelled()
                inputGiven = True
            else:
                utils.outputText.invalidInput()
                textoverride = input(utils.user_label() + " ").lower()
    else:
        messagesSent.append({
            "role": "user",
            "content": anonymizer_results.text
        })

    if len(messagesSent) > 0:
        completion = client.chat.completions.create(
            messages=messagesSent,
            model=selectedModel,
            stream=True,
        )
        print(utils.assistant_label(), end=" ")
        for chunk in completion:
            print(chunk.choices[0].delta.content or "", end="")
            sleep(0.02)
        print("")
        