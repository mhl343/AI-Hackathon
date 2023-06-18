import streamlit as st
import pandas as pd
import numpy as np
import openai 
import json



def app():
    st.header("Hello! \U0001F44B I'm Fiona.")
    openai.api_key = "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"

    with open('sample.json') as json_file:
        data = json.load(json_file)

    def format_prompt():
        user_prompt = f"""User's journal entry on day {data["date"]}: {data["entry"]}\n
                        Top Emotions Expressed: Sadness, Hope, Disappointment
                        """
        return user_prompt
        
    messages = [
    {"role": "system", "content": "You are a mental health counselor  for this user. The Top Emotions Expressed category shows the top emotions that the user expresses in the current day’s journal entry. Use this category to inform  your tone and advice."}
    ]

    @st.cache_data
    def generate_response(question):
        # Add user input to messages/dialogue history
        messages.append({'role': 'user', 'content': question})

        # Generate response using OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Extract the assistant's response
        content = response['choices'][0]['message']['content']

        # Add assistant's response to messages/dialogue history
        messages.append({'role': 'assistant', 'content': content})

        return content

    st.write("Fiona's advice from your journal entry...")
    initial_response = generate_response(format_prompt())
    st.write(initial_response)

    def chat():
        '''
        Tracks dialogue history and takes in user input
        '''
        count = 1
        st.text('To end conversation, type END')
        question = ''

        while question != 'END':
            question = st.text_input("Enter your text here", key=f"user_input{count}")

            while not question:
                continue
            content = generate_response(question)
            st.write(content)

            messages.append({'role':'assistant','content':content})
            count += 1
    st.write("\n")
    if st.button("Click here to speak with Fiona!"):
        chat()