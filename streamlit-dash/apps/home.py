import streamlit as st
from streamlit_lottie import st_lottie
import json

def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

def app():

    #st.title("welcome to dailyfi \U0001F430")
    lottie_home = load_lottiefile("data/home.json")

    col1, col2 = st.columns(2)
    with col1:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.title("welcome to...") 
        st.title("dailyfi \U0001F430")
    with col2:
        st_lottie(
            lottie_home,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium",
            height=None,
            width=None,
            key="lottie_home"
        )
    st.subheader("check out our different resources!")
        
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://img.freepik.com/premium-vector/cute-happy-alarm-clock-pour-milk-into-cereal-flat-line-cartoon-kawaii-character-icon-hand-drawn-style-illustration-isolated-white-background_92289-2049.jpg?w=2000", width = 200)
        st.title("-----")
        st.markdown("#### track your **:blue[habits]**")
        st.markdown("###### create a checklist of healthy habits you want to start implementing in your life")

    with col2:
        st.image("https://i.pinimg.com/474x/39/19/f8/3919f8ae145eea7c786abd46b2807bea.jpg", width = 200)
        st.title("-----")
        st.markdown("#### :blue[journaling] space")
        st.markdown("###### journal all your thoughts away in this safe space")

    with col3:
        st.image("https://i.pinimg.com/564x/78/64/bc/7864bc7632a0abf7905f7736d432c5bc--dont-forget-bunny.jpg", width = 260)
        st.title("-----")
        st.markdown("#### :blue[chat] with a friend")
        st.markdown(" ###### talk it out with our friendly chatbot, fiona!")