import streamlit as st
import pandas as pd

def app():
    st.title("Let's Pick a Song for You!")
    day = st.text_input('Describe how you are feeling!')

    #def load_data():
    #dfplayers = pd.read_csv("data/deals.csv", index_col=0)
    #return dfplayers