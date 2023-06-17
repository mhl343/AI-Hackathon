import pandas as pd 
import streamlit as st 
from multiapp import MultiApp
from apps import display, home, predict

def local_css():
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css()
app = MultiApp()
app.add_app("Homepage", home.app)
app.add_app("Display", display.app)
app.add_app("Predict", predict.app)

app.run()