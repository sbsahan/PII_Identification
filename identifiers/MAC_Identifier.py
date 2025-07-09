print("MAC_Identifier.py loaded")

from presidio_analyzer import Pattern, PatternRecognizer
import config

class MACRecognizer(PatternRecognizer):
    def __init__(self):
        patterns = [Pattern("MAC Pattern", config.patterns.mac_addresses, 0.5)]
        super().__init__(supported_entity="MAC", 
                         supported_language="en", 
                         patterns=patterns,
                         context=config.context.medications)
