import streamlit as st
from chatbot_engine import get_chatbot_response

st.set_page_config(
    page_title="Medical Chatbot",
    page_icon="🩺",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("⚙️ Settings")

    dev_mode = st.toggle("Developer Mode (Show Intent & Confidence)", value=True)

    st.markdown("---")
    st.info("🩺 Medical FAQ Chatbot using TF-IDF + Fuzzy Matching + Intent Detection")

# ---------------- MAIN UI ----------------
st.title("🩺 Medical FAQ Chatbot")
st.caption("Ask any medical question and get instant answers")

# Session memory for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your medical question here...")

# ---------------- PROCESS INPUT ----------------
if user_input:
    response = get_chatbot_response(user_input)

    st.session_state.chat_history.append({
        "user": user_input,
        "bot": response
    })

# ---------------- DISPLAY CHAT ----------------
for chat in st.session_state.chat_history:
    user_msg = chat["user"]
    bot = chat["bot"]

    # USER MESSAGE
    with st.chat_message("user"):
        st.write(user_msg)

    # BOT MESSAGE
    with st.chat_message("assistant"):
        st.markdown(f"**🧠 Answer:** {bot['answer']}")

        # Developer Mode Section
        if dev_mode:
            col1, col2 = st.columns(2)

            with col1:
                st.metric("Intent", bot["intent"])

            with col2:
                st.metric("Confidence", f"{bot['confidence']*100:.1f}%")

            st.caption(f"Matched FAQ: {bot['matched_question']}")