import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="SakhiAI 🌸", page_icon="🌸")

st.title("🌸 SakhiAI – Aapki Friendly Saheli")
st.write(
    "Main aapki madad karungi cooking, movies, Gen-Z words aur daily life ke chhote-chhote doubts mein 😊"
)

# ---------------- HUGGING FACE CONFIG ----------------
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"

HF_TOKEN = st.secrets["HF_TOKEN"]   # MUST exist in Secrets
HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def call_hf(prompt):
    try:
        response = requests.post(
            API_URL,
            headers=HEADERS,
            json={"inputs": prompt},
            timeout=60
        )
        return response.json()
    except Exception:
        return None

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY CHAT HISTORY ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Aaj kya poochhna hai? 😊")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prompt design (millennial mom tone)
    prompt = f"""
You are SakhiAI, a friendly assistant for Indian millennial mothers.
Tone: warm, modern, respectful, supportive — like a saheli.
Language: simple Hinglish.
Avoid words like beta, baccha.
Be practical and clear.

Question: {user_input}
Answer:
"""

    # Call model with spinner
    with st.chat_message("assistant"):
        with st.spinner("SakhiAI soch rahi hai… 🤔"):
            result = call_hf(prompt)

        # -------- SAFE RESPONSE HANDLING --------
        reply = None

        if isinstance(result, list):
            if len(result) > 0 and "generated_text" in result[0]:
                reply = result[0]["generated_text"]

        if reply is None:
            reply = (
                "Main thodi der mein ready ho jaungi 😊 "
                "Free AI model kabhi-kabhi slow ho jata hai. "
                "30–60 seconds baad phir try karna."
            )

        st.markdown(reply)

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
