# 🩺 Medical FAQ Chatbot


An intelligent chatbot system that answers medical FAQs using TF-IDF vectorization, fuzzy matching, and intent detection. No training required—just ask!

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/medical-chatbot.git
cd medical-chatbot
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Chatbot
```bash
streamlit run streamlit_app.py
```

That's it! 🎉 Your chatbot will open at `http://localhost:8501`

---

## 💬 Try It Out

Once running, ask questions like:
- "How much does knee replacement surgery cost?"
- "What are the symptoms of diabetes?"
- "How does heart surgery work?"
- "When should I schedule an appointment?"

The chatbot will:
- 🧠 Detect medical intent
- 🔍 Find the best matching FAQ
- 📊 Show confidence score
- ✅ Return the answer

---

## 📁 Project Structure

```
medical-chatbot/
├── streamlit_app.py          # 🎨 Main UI (Streamlit)
├── chatbot_engine.py         # 🧠 Core logic
├── search_engine.py          # 🔍 FAQ retrieval (TF-IDF + Fuzzy)
├── intent_detector.py        # 🎯 Intent classification
├── app.py                    # ⚙️ Flask backend (optional)
├── requirements.txt          # 📦 Dependencies
├── data/
│   ├── faq_dataset.json      # 📚 Medical FAQs (~100+ Q&As)
│   └── synonyms.json         # 🏷️ Intent keywords
└── README.md
```

---

## 🛠️ How It Works

### The Matching Algorithm

The system uses a **hybrid approach** to find the best FAQ answer:

```
User Query
    ↓
├─→ TF-IDF Similarity (70% weight)
│   └─ Semantic meaning of question
│
├─→ Fuzzy String Matching (30% weight)
│   └─ Character-level similarity
│
└─→ Final Confidence Score
    └─ Weighted combination of both
```

**Example:**
- Query: "What's the cost of knee surgery?"
- Best Match: "How much does knee replacement surgery cost?"
- Confidence: 0.87 (87%)

---

## 📋 Features

✨ **Smart Matching** - TF-IDF + Fuzzy Matching hybrid algorithm  
🧠 **Intent Detection** - Identifies medical categories (cost, symptoms, treatment, etc.)  
📊 **Confidence Scoring** - Know how confident the answer is (0-100%)  
🎨 **Beautiful UI** - Modern Streamlit interface with chat history  
👨‍💻 **Developer Mode** - See intent and matched FAQ for debugging  
🔄 **Easy to Extend** - Add new FAQs without retraining  
⚡ **No GPU Needed** - Runs on any machine  

---

## 📦 Requirements

```
flask
scikit-learn
rapidfuzz
numpy
pandas
streamlit
```

Or install from `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 🎯 Example Usage

### In Terminal
```bash
streamlit run streamlit_app.py
```

### As Python Library
```python
from chatbot_engine import get_chatbot_response

response = get_chatbot_response("How much does heart surgery cost?")

print("Answer:", response['answer'])
print("Intent:", response['intent'])
print("Confidence:", response['confidence'])
print("Matched FAQ:", response['matched_question'])
```

**Output:**
```
Answer: Heart bypass surgery typically costs between $6000 and $12000.
Intent: treatment_cost
Confidence: 0.91
Matched FAQ: What are the charges for heart bypass surgery?
```

### With Flask
```bash
python app.py
```

Then POST to `http://localhost:5000/chat`:
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is diabetes?"}'
```

---

## 🎨 User Interface

The Streamlit app features:

- 💬 Chat interface with message history
- ⚙️ Developer Mode toggle
- 🎯 Intent detection display
- 📊 Confidence score visualization
- 🩺 Medical chatbot branding

### Developer Mode
When enabled, shows:
- Detected intent category
- Confidence percentage
- Matched FAQ question (source)

---

## ⚙️ Configuration

### Add New FAQs

Edit `data/faq_dataset.json`:

```json
[
  {
    "intent": "treatment_cost",
    "question": "How much does X cost?",
    "answer": "X costs between $Y and $Z..."
  },
  {
    "intent": "symptoms",
    "question": "What are symptoms of X?",
    "answer": "Symptoms of X include..."
  }
]
```

### Add New Intent Categories

Edit `data/synonyms.json`:

```json
{
  "my_new_intent": [
    "keyword1",
    "keyword2",
    "keyword3"
  ]
}
```

**No retraining needed!** Changes take effect on next restart.

---

## 🧪 Testing

### Test Intent Detection
```python
from intent_detector import detect_intent

print(detect_intent("How much does surgery cost?"))
# Output: treatment_cost
```

### Test FAQ Search
```python
from search_engine import search_faq

faq, confidence = search_faq("Cost of knee surgery")
print(f"Answer: {faq['answer']}")
print(f"Confidence: {confidence}")
```

---

## 🔧 Customize Matching Weights

In `search_engine.py` line 23:

```python
# Current: 70% semantic, 30% fuzzy
final_score = (best_score * 0.7) + (fuzzy_score * 0.3)

# To prioritize semantic matching (80% semantic, 20% fuzzy):
final_score = (best_score * 0.8) + (fuzzy_score * 0.2)

# To prioritize fuzzy matching (50% semantic, 50% fuzzy):
final_score = (best_score * 0.5) + (fuzzy_score * 0.5)
```

---

## ⚠️ Limitations

- **FAQ-based only** - Answers limited to pre-defined database
- **No deep learning** - Uses traditional NLP (not transformers)
- **Keyword intent** - Intent detection based on simple keyword matching
- **No context memory** - Each query is independent
- **English only** - Primarily designed for English

---

## 💡 Use Cases

✅ **Healthcare Portals** - FAQ chatbot for hospital websites  
✅ **Insurance Companies** - Answer patient queries 24/7  
✅ **Wellness Apps** - Quick medical information lookup   
✅ **Telemedicine** - Pre-consultation chatbot  

---



