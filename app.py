
import streamlit as st

from chatbot import FAQChatbot
from faq_data import FAQ_DATA


st.set_page_config(
    page_title="Campus FAQ Chatbot",
    page_icon="🎓",
    layout="centered"
)


@st.cache_resource
def load_chatbot():
    """Create and cache the FAQ chatbot."""
    return FAQChatbot(threshold=0.45)


chatbot = load_chatbot()


st.title("🎓 Campus FAQ Chatbot")
st.write(
    "Ask a question about admissions, fees, attendance, "
    "exams, library services, placements, and more."
)

st.caption("This chatbot uses TF-IDF and cosine similarity to find answers.")


# Sidebar
with st.sidebar:
    st.header("About")
    st.write(
        "A retrieval-based FAQ chatbot built with Python, "
        "Streamlit, and scikit-learn."
    )

    st.subheader("Try these questions")

    sample_questions = [
        "How can I apply for admission?",
        "I forgot my password",
        "Where can I check my exam timetable?",
        "How can I register for placements?",
        "How do I borrow library books?"
    ]

    for question in sample_questions:
        if st.button(question, use_container_width=True):
            st.session_state.pending_question = question

    st.divider()

    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.pending_question = None
        st.rerun()


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant" and "category" in message:
            st.caption(
                f"Category: {message['category']} "
                f"| Similarity: {message['score']:.3f}"
            )


# Chat input
user_question = st.chat_input("Type your question here...")


# Handle a typed question or sidebar sample question
question_to_process = (
    user_question
    or st.session_state.pending_question
)

if question_to_process:
    st.session_state.pending_question = None

    # Display and save the user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question_to_process
        }
    )

    with st.chat_message("user"):
        st.markdown(question_to_process)

    # Generate the FAQ response
    result = chatbot.get_response(question_to_process)

    with st.chat_message("assistant"):
        st.markdown(result["answer"])
        st.caption(
            f"Category: {result['category']} "
            f"| Similarity: {result['score']:.3f}"
        )

    # Save assistant response to chat history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"],
            "category": result["category"],
            "score": result["score"]
        }
    )

