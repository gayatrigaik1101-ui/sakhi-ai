import streamlit as st
import requests

# Page config
st.set_page_config(page_title="SakhiAI 🌸", page_icon="🌸")

# Title & intro
st.title("🌸 SakhiAI – Aapki Friendly Saheli")
st.write(
    "Main aapki madad karungi cooking, movies, Gen-Z words aur daily life ke chhote-chhote doubts mein 😊"
)

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
HEADERS = {
    "Authorization": f"Bearer {st.secrets['HF_TOKEN']}"
}

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Aaj kya poochhna hai? 😊")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prompt (millennial mom tone)
    prompt = f"""
    You are SakhiAI, a friendly assistant designed for Indian millennial mothers.
    Your tone is warm, modern, respectful, and supportive — like a helpful saheli.
    Speak in simple Hinglish.
    Avoid words like "beta" or overly parental language.
    Be practical and clear.

    Question: {user_input}
    Answer:
    """
    with st.spinner("SakhiAI soch rahi hai… 🤔"):
        result = query({"inputs": prompt})

# Handle Hugging Face responses properly
if isinstance(result, list) and result and "generated_text" in result[0]:
    reply = result[0]["generated_text"]

elif isinstance(result, dict) and result.get("error"):
    reply = (
        "Main thodi der mein ready ho jaungi 😊 "
        "Model load ho raha hai, 30–60 seconds baad phir try karo."
    )

else:
    reply = (
        "Ek chhota sa wait lagega 😊 "
        "Free AI model thoda slow hota hai. Thodi der baad phir poochna."
    )

    

   
