import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="SakhiAI 🌸", page_icon="🌸")

st.title("🌸 SakhiAI – Aapki Friendly Saheli")
st.write(
    "Main aapki madad karungi cooking, movies, Gen-Z words aur daily life ke common doubts mein 😊"
)

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SMART HYBRID LOGIC ----------------
def sakhi_reply(user_text):
    text = user_text.lower()

    # 🍳 COOKING – PANEER
    if "paneer" in text and "soft" in text:
        return (
            "Paneer soft rakhne ke liye ek simple trick hai 😊\n\n"
            "• Paneer ko 10–15 minute garam paani mein soak kar do\n"
            "• Cooking se pehle halka sa squeeze kar lo\n"
            "• Zyada der fry mat karo\n\n"
            "Isse paneer kaafi soft rehta hai 👍"
        )

    if "paneer" in text and ("recipe" in text or "sabzi" in text):
        return (
            "Quick paneer sabzi recipe 😊\n\n"
            "1️⃣ Oil + jeera\n"
            "2️⃣ Onion-tomato paste bhuno\n"
            "3️⃣ Haldi, mirchi, dhania powder\n"
            "4️⃣ Paneer cubes add karo\n"
            "5️⃣ Thoda cream ya milk\n\n"
            "5 minute mein tasty sabzi ready 💛"
        )

    # 🍞 ROTI / CHAPATI
    if "roti" in text or "chapati" in text:
        return (
            "Roti soft banane ke liye yeh try karo 👇\n\n"
            "• Aata thoda gungune paani se gundho\n"
            "• Thoda oil add karo\n"
            "• 10 minute rest do\n\n"
            "Roti soft aur fluffy banegi 😊"
        )

    # 👶 PARENTING / DAILY LIFE
    if "screen time" in text or "mobile" in text:
        return (
            "Screen time kam karne ke liye simple steps 😊\n\n"
            "• Fixed timing decide karo\n"
            "• Khud bhi phone kam use karo\n"
            "• Outdoor ya hobby activities introduce karo\n\n"
            "Slow changes zyada effective hote hain 👍"
        )

    if "tired" in text or "thakaan" in text:
        return (
            "Aisa feel hona bilkul normal hai 💛\n\n"
            "• Thoda rest lo\n"
            "• Paani zyada piyo\n"
            "• Apne liye 15 minute nikalo\n\n"
            "Aap akeli nahi ho 😊"
        )

    # 🎬 MOVIES
    if "movie" in text:
        return (
            "Aaj ke liye kuch achhi movie suggestions 🎬\n\n"
            "• English: The Intern\n"
            "• Hindi: English Vinglish\n"
            "• Family: Kapoor & Sons\n\n"
            "Mood ke hisaab se perfect choices 😊"
        )

    # 🧠 GEN-Z WORDS
    if "slay" in text:
        return (
            "‘Slay’ ka matlab hota hai — bahut accha karna 😄\n\n"
            "Example: ‘You slayed that outfit!’\n"
            "Matlab: outfit bahut achha lag raha hai ✨"
        )

    if "genz" in text or "gen z" in text:
        return (
            "Gen-Z words thode confusing ho sakte hain 😄\n\n"
            "• Slay = awesome\n"
            "• Sus = suspicious\n"
            "• Chill = relax\n\n"
            "Slow-slow aadat ho jaati hai 😊"
        )

    # 💬 GREETINGS
    if "hello" in text or "hi" in text:
        return "Hello 😊 Kaise ho? Aaj kya poochhna hai?"

    # 🔁 DEFAULT RESPONSE
    return (
        "Yeh interesting sawaal hai 😊\n"
        "Abhi main common daily-life cheezon mein madad karti hoon.\n\n"
        "Agar cooking, movies, Gen-Z words ya daily routine se related ho, "
        "toh zaroor poochna 🌸"
    )

# ---------------- DISPLAY CHAT HISTORY ----------------
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

    reply = sakhi_reply(user_input)

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
