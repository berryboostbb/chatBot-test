from intent_detector import detect_intent
from search_engine import search_faq

def get_chatbot_response(message):
    intent = detect_intent(message)

    faq, confidence = search_faq(message)

    return {
        "intent": intent,
        "confidence": confidence,
        "matched_question": faq["question"],
        "answer": faq["answer"]
    }
