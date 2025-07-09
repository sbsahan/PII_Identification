print("Medication_Identifier.py loaded")

from presidio_analyzer import PatternRecognizer
import config

class MedicationRecognizer(PatternRecognizer):
    def __init__(self):
        super().__init__(supported_entity="MEDS", 
                         supported_language="en", 
                         deny_list=config.deny_lists.medications, 
                         context=config.context.medications)
