from presidio_analyzer import PatternRecognizer, Pattern, RecognizerResult
import config

class TCKNRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern("TCKN Pattern", config.patterns.tckn, 0.5)]
        super().__init__(supported_entity="TCKN", 
                         patterns=patterns, 
                         supported_language="en")

    def validate_result(self, result: RecognizerResult) -> bool:
        tckn = result
        if not tckn.isdigit() or len(tckn) != 11:
            return False

        digits = list(map(int, tckn))
        if digits[0] == 0:
            return False

        digit10 = ((sum(digits[0:10:2]) * 7) - sum(digits[1:9:2])) % 10
        digit11 = sum(digits[:10]) % 10

        return digits[9] == digit10 and digits[10] == digit11
