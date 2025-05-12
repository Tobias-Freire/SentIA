import streamlit as st
from streamlit_autorefresh import st_autorefresh
from kafkadir.utils import get_topics
from kafkadir.producer import send_message
from kafkadir.consumer import consume_latest_message

st.set_page_config(page_title="Kafka Demo", layout="centered")
st.title("Kafka Demo")

# Auto refresh interface every 5 seconds
st_autorefresh(interval=5000, key="consumer_refresh")

topics = get_topics()

# ------------------ Producer Section ------------------
st.header("Producer")

producer_topic = st.selectbox("Select a topic to produce to:", options=topics, key="producer_topic")
key = st.text_input("Key", key="key")
value = st.text_input("Value", key="value")

if st.button("Send message"):
    send_message(producer_topic, key, value)
    st.success("Message sent!")

# ------------------ Consumer Section ------------------
st.header("Consumer")

selected_topic = st.selectbox("Select a topic to consume from:", options=topics, key="consumer_topic")

# Reset messages if topic changes
if "last_topic" not in st.session_state or st.session_state.last_topic != selected_topic:
    st.session_state.last_topic = selected_topic
    st.session_state.messages = []

# Consume new messages
new_message = consume_latest_message(selected_topic)
st.session_state.new_message = new_message

# ------------------ Display ------------------
if st.session_state.new_message:
    st.json(st.session_state.new_message)
else:
    st.info("No messages found in this topic.")
