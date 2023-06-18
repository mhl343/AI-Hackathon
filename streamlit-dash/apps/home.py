import streamlit as st
import pandas as pd

def app():

    st.title("Welcome to the mental health hub!")
    st.header("Check our our different resources!")
        
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Track your Habits!")
        st.image("https://images.vexels.com/media/users/3/128840/isolated/preview/c091629800ce3d91d8527d32d60bc46f-stopwatch-timer.png")

    with col2:
        st.header("Journaling Space")
        st.image("https://cdn.pixabay.com/photo/2014/04/03/00/32/notebook-308615_1280.png")

    with col3:
        st.header("Chat With a Friend!")
        st.image("https://static.vecteezy.com/system/resources/previews/009/385/411/non_2x/chat-box-clipart-design-illustration-free-png.png")
