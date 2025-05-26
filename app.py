import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Medical DefyBot", layout="wide")
st.title("🩺 Medical DefyBot (Embedded)")

bot_url = "https://udify.app/chat/5eZTphEjfR6KQPJx"

components.iframe(
    bot_url,
    height=600,
    scrolling=True
)