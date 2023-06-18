import pandas as pd 
import streamlit as st 
from multiapp import MultiApp
from apps import habits, home, chatbot, song

def local_css():
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css()

app = MultiApp()
app.add_app("Homepage", home.app)
app.add_app("Habits", habits.app)
app.add_app("Chatbot", chatbot.app)
app.add_app("Song", song.app)

app.run()