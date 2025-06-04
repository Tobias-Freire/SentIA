import streamlit as st
from src.kafka_producer import create_producer, send_message
from src.config import topics

producer = create_producer()

st.write("""
# Feedback Page
""")
st.text_input("Provide your feedback", key="feedback_input")
if st.button("Submit Feedback"):
    feedback = st.session_state.feedback_input
    if feedback:
        send_message(producer, topics[0], feedback)
        st.success("Feedback submitted successfully!")
    else:
        st.error("Please enter some feedback before submitting.")