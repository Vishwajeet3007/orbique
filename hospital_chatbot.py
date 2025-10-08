import streamlit as st

# 20 Receptionist Questions including "exit" question
questions = [
    "What is your full name?",
    "What is your age?",
    "What is your gender?",
    "What is your date of birth?",
    "What is your phone number?",
    "What is your address?",
    "Do you have any allergies?",
    "What are your current symptoms?",
    "When did the symptoms start?",
    "Do you have any chronic conditions?",
    "Are you taking any medications?",
    "Have you had recent surgeries?",
    "What is the reason for your visit today?",
    "Have you visited our hospital before?",
    "Do you have a health insurance policy?",
    "What is your insurance provider name?",
    "Do you have a preferred doctor?",
    "Are you experiencing any pain now?",
    "Have you traveled recently?",
    "Is there anything else we should know?",
    "Would you like to exit now?",  # <-- exit is treated as a question here
]

# Initialize session state
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "chat_active" not in st.session_state:
    st.session_state.chat_active = True

# App Title
st.title("🏥 Hospital Receptionist Chatbot")
st.write("I will ask you a few questions. Please type your answers one by one.")
st.write("ℹ️ Note: Type `exit` anytime to stop the chat early.")

# Chat logic
if st.session_state.chat_active:
    if st.session_state.current_q < len(questions):
        current_question = questions[st.session_state.current_q]
        st.markdown(f"**Question {st.session_state.current_q + 1} of {len(questions)}:** {current_question}")

        answer = st.text_input("Your answer:", key=f"answer_{st.session_state.current_q}")

        if answer:
            if answer.strip().lower() == "exit":
                st.session_state.chat_active = False
                st.warning("❌ You ended the session by typing 'exit'.")
            else:
                # Save the answer and move to the next question
                st.session_state.answers[current_question] = answer
                st.session_state.current_q += 1
                st.rerun()
    else:
        # All questions completed
        st.success("✅ You have answered all questions.")
        st.session_state.chat_active = False

# Show summary if chat has ended
if not st.session_state.chat_active:
    if st.session_state.answers:
        st.markdown("---")
        st.markdown("### 📝 Your Information Summary:")
        for i, question in enumerate(questions[:len(st.session_state.answers)]):
            answer = st.session_state.answers.get(question, "Not answered")
            st.markdown(f"**{i+1}. {question}**  \n➡️ {answer}")
    else:
        st.info("No answers were provided.")

    st.markdown("---")
    st.markdown("🔄 *Refresh the page to restart the chatbot.*")
