import streamlit as st
import pandas as pd
import numpy as np
import openai 

def app():
    st.header("Predict")
    openai.api_key = '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 '
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
        ]
    def chat():
        '''
        Tracks dialogue history and takes in user input
        '''
        print('To end conversation, type END')
        question = ''
        while question != 'END':
            # Get User Question
            user_input = st.text_input("Enter your text here", key="user_input")
            #question = input("")
            question = user_input
            
            # Add to messages/dialogue history
            messages.append({'role':'user','content':question})

            #Send to ChatGPT and get response
            response = openai.ChatCompletion.create(
                  model="gpt-3.5-turbo",
                  messages=messages)

            # Get content of assistant reply
            content = response['choices'][0]['message']['content']
            st.write(content)
        
            # Add assistant reply for dialogue history
            messages.append({'role':'assistant','content':content})

    chat()

