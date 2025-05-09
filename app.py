# app.py

import streamlit as st
from npc_bot import npc_chat

st.set_page_config(page_title="NPC Wizard Chat")
st.title("🧙 Chat with Thalorion the Timeless")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

if user_input:
    response = npc_chat(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Thalorion the Timeless", response))

for speaker, message in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {message}")
