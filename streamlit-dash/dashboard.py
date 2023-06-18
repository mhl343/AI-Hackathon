import streamlit as st 
from multiapp import MultiApp
from apps import habits, home, chatbot, song, habits_log

def local_css():
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css()

app = MultiApp()
app.add_app("homepage", home.app)
app.add_app("dashboard", habits.app)
app.add_app("habits log", habits_log.app)
app.add_app("chat with a friend!", chatbot.app)


app.run()