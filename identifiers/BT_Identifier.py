import utils

utils.dim("BT_Recognizer loaded")

from presidio_analyzer import PatternRecognizer
import config

class BTRecognizer(PatternRecognizer):
    def __init__(self):
        super().__init__(supported_entity="BT", 
                         supported_language="en", 
                         deny_list=config.deny_lists.blood_types, 
                         context=config.context.blood_types)
