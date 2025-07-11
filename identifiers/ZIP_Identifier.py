print("ZIP_Identifier.py loaded")

from presidio_analyzer import Pattern, PatternRecognizer
import config

class MedicationRecognizer(PatternRecognizer):
    def __init__(self):
        patterns = [Pattern("MAC Pattern", config.patterns.zip_codes, 0.01)]
        super().__init__(supported_entity="ZIP_CODE", 
                         supported_language="en", 
                         patterns=patterns, 
                         context=config.context.zip_codes)
