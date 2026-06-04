import json
from rapidfuzz import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("data/faq_dataset.json", "r") as f:
    FAQS = json.load(f)

questions = [faq["question"] for faq in FAQS]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(questions)

def search_faq(user_query):
    query_vector = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

    best_index = similarities.argmax()
    best_score = similarities[best_index]

    fuzzy_score = fuzz.ratio(user_query.lower(), questions[best_index].lower()) / 100

    final_score = (best_score * 0.7) + (fuzzy_score * 0.3)

    return FAQS[best_index], round(final_score, 2)
