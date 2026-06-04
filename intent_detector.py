import json

with open("data/synonyms.json", "r") as f:
    SYNONYMS = json.load(f)

def detect_intent(message):
    message = message.lower()

    for intent, keywords in SYNONYMS.items():
        for keyword in keywords:
            if keyword in message:
                return intent

    return "unknown"
