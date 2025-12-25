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
HF_TOKEN = st.secrets["HF_TOKEN"]

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

# ---------------- PREDEFINED (FAST) ANSWERS ----------------
def static_reply(user_text):
    text = user_text.lower()

    if "paneer" in text and "soft" in text:
        return (
            "Paneer soft rakhne ke liye ek simple tip hai 😊\n\n"
            "• Paneer banane ya laane ke baad use 10–15 minute garam paani mein soak kar do\n"
            "• Cooking se pehle lightly squeeze kar lo\n"
            "• Zyada der fry mat karo – paneer hard ho jata hai\n\n"
            "Isse texture kaafi soft rehta hai 👍"
        )

    if "paneer recipe" in text or "paneer ki recipe" in text:
        return (
            "Quick paneer sabzi idea 😊\n\n"
            "1️⃣ Thoda oil + jeera\n"
            "2️⃣ Onion–tomato paste bhuno\n"
            "3️⃣ Haldi, mirchi, dhania powder\n"
            "4️⃣ Paneer cubes daal kar 2–3 min cook\n"
            "5️⃣ Thoda cream ya milk add karo\n\n"
            "Simple & tasty 💛"
        )

    return None  # means AI should handle it

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SHOW CHAT HISTORY ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Aaj kya poochhna hai? 😊")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # 🔥 FIRST TRY STATIC LOGIC
    reply = static_reply(user_input)

    # 🤖 IF NO STATIC ANSWER → AI
    if reply is None:
        prompt = f"""
You are SakhiAI, a friendly assistant for Indian millennial mothers.
Tone: warm, modern, respectful, supportive.
Language: simple Hinglish.
Avoid parental words like beta.

Question: {user_input}
Answer:
"""
        with st.chat_message("assistant"):
            with st.spinner("SakhiAI soch rahi hai… 🤔"):
                result = call_hf(prompt)

            reply = None
            if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
                reply = result[0]["generated_text"]

            if reply is None:
                reply = (
                    "Main thodi der mein ready ho jaungi 😊 "
                    "Free AI model kabhi-kabhi slow hota hai. "
                    "Thodi der baad phir try karna."
                )

            st.markdown(reply)
    else:
        with st.chat_message("assistant"):
            st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
