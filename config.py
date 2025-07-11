class groqConf:
    api_key = ""  # Replace with your actual Groq API key
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
    selectedModel = "compound-beta"

class deny_lists:
    medications = [
        "acetaminophen", "ibuprofen", "aspirin", "amoxicillin", 
        "penicillin", "erythromycin", "clindamycin", "metronidazole", 
        "ciprofloxacin", "morphine", "codeine", "diazepam", "lorazepam", 
        "sertraline", "fluoxetine", "metformin", "insulin", 
        "salbutamol", "prednisolone", "tylenol", "advil", "aleve"
    ]
    blood_types = [
        "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-",
        "A positive", "A negative", "B positive", "B negative",
        "AB positive", "AB negative", "O positive", "O negative"
    ]

class context:
    medications = [
        "prescription", "use", "take", "took", "taking", "using"
    ]
    blood_types = [
        "blood", "type", "group"
    ]
    mac_addresses = [
        "mac", "address", "network", "device", "wifi"
    ]
    zip_codes = [
        "zip", "code", "postalcode", "zipcode"
    ]

class patterns:
    mac_addresses = r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})'
    tckn = r'\b[1-9][0-9]{9}[02468]\b'
    zip_codes = r'\b\d{5}\b'
