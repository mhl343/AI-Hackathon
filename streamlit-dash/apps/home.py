import streamlit as st
import pandas as pd

def app():

    st.title("welcome to fifi chat \U0001F430")
    st.header("check out our different resources!")
        
    col1, col2, col3 = st.columns(3)

    with col1:
        st.text("--")
        st.image("https://images.vexels.com/media/users/3/128840/isolated/preview/c091629800ce3d91d8527d32d60bc46f-stopwatch-timer.png")
        st.subheader("track your habits!")

    with col2:
        st.text("--")
        st.image("https://cdn.pixabay.com/photo/2014/04/03/00/32/notebook-308615_1280.png")
        st.subheader("journaling space")

    with col3:
        st.text("--")
        st.image("https://static.vecteezy.com/system/resources/previews/009/385/411/non_2x/chat-box-clipart-design-illustration-free-png.png")
        st.subheader("chat with a friend!")