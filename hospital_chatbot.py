import streamlit as st
import re

# --- Page Setup ---
st.set_page_config(page_title="Hospital Chatbot", page_icon="🏥", layout="centered")

st.title("🏥 Hospital Chatbot")
st.write("Hi! I’m your hospital assistant. Ask me anything about hospital services, timings, or appointments.")

# --- Initialize chat state ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chat_running" not in st.session_state:
    st.session_state.chat_running = True

# --- Knowledge Base ---
hospital_data = [
    {"keywords": ["hello", "hi", "hey"], "response": "Hello! How can I help you today?"},
    {"keywords": ["timing", "open", "hours", "time"], "response": "We are open 24/7 for emergencies. OPD runs from 9 AM to 6 PM."},
    {"keywords": ["visiting", "visit", "visitor"], "response": "Visiting hours are from 9 AM to 8 PM every day."},
    {"keywords": ["appointment", "book", "schedule", "meeting", "consultation"], "response": "You can book an appointment by calling +1-800-HOSPITAL or visiting our website."},
    {"keywords": ["location", "address", "where"], "response": "We are located at 123 Health Street, MedCity."},
    {"keywords": ["emergency", "urgent", "24/7", "accident"], "response": "Yes, our emergency department is open 24/7."},
    {"keywords": ["doctor", "specialist", "available", "department"], "response": "We have specialists in cardiology, neurology, orthopedics, pediatrics, and general medicine."},
    {"keywords": ["checkup", "test", "screening", "health package"], "response": "You can visit our Health Checkup Center between 8 AM and 4 PM. Booking is recommended."},
    {"keywords": ["thank", "thanks"], "response": "You're welcome! Happy to help."},
    {"keywords": ["bye", "goodbye", "see you"], "response": "Goodbye! Take care and stay healthy."},
    {"keywords": ["best hospital", "top hospital", "famous hospital", "which hospital", "hospital in india"], "response": "Some of the top hospitals in India include AIIMS Delhi, Apollo Hospitals, Fortis, and Medanta. Each excels in different specialties."}
]

# --- Function: Show Q&A Summary ---
def generate_qa_summary():
    summary = "### 💬 Chat Summary (Questions & Answers Only)\n\n"
    qas = []
    for i in range(0, len(st.session_state.chat_history) - 1, 2):
        user_msg = st.session_state.chat_history[i]
        bot_msg = st.session_state.chat_history[i + 1]
        if user_msg["role"] == "user" and bot_msg["role"] == "bot":
            qas.append(f"**Q{i//2 + 1}.** {user_msg['content']}\n**A:** {bot_msg['content']}\n")
    if qas:
        summary += "\n".join(qas)
    else:
        summary += "_No questions were asked._"
    return summary

# --- Display chat history ---
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Chatbot:** {msg['content']}")

# --- Chat input ---
if st.session_state.chat_running:
    user_message = st.chat_input("Type your message...")

    if user_message:
        st.session_state.chat_history.append({"role": "user", "content": user_message})
        query = user_message.lower().strip()

        # Exit command
        if query in ["exit", "quit", "end"]:
            summary_message = generate_qa_summary()
            st.session_state.chat_history.append({"role": "bot", "content": summary_message})
            st.session_state.chat_running = False
        else:
            response = None
            for entry in hospital_data:
                for keyword in entry["keywords"]:
                    if re.search(rf"\b{re.escape(keyword)}\b", query):
                        response = entry["response"]
                        break
                if response:
                    break
            if not response:
                response = "I'm sorry, I don't have information about that. Please contact our help desk at +1-800-HOSPITAL."
            st.session_state.chat_history.append({"role": "bot", "content": response})

        st.rerun()

else:
    st.success("✅ Chat ended. Click the **Rerun** button (top-right) to start again.")
