import streamlit as st
import pandas as pd
import math
from datetime import date
import json

def add_habit(new_habit):
    global habit_list
    habit_list.append(new_habit)

habit_list = []

def app():
    st.header("Today's Habit Tracker")
    c1, c2, c3, c4 = st.columns(4)

    new_habit = st.text_input("Add a habit! (e.g. sleep 8+ hours, eat 3 meals, walk 10k steps)", key="new_habit")
    
    if st.button("Add", on_click=add_habit, args=(new_habit,)):
        pass

    counter = 1
    col = 0
    for habit in habit_list:
        if col == 0:
            curr = c1
        if col == 1:
            curr = c2
        elif col == 2:
            curr = c3
        if col == 3:
            curr = c4

        with curr:
            st.checkbox(habit, key = f"box{counter}")
        col = (col + 1) % 4
        counter += 1

#--------------journaling----------------
    st.header("journaling...")

    col1, col2 = st.columns([3, 1])
    
    with col2:
        type = st.radio("how would you like to document today's journal entry?",
                        ('text box', 'video', 'voice memo', 'image'))
    
    with col1:
        st.write(f"Date: {date.today()}")
        if type == 'text box':
            entry = st.text_area("today's journal entry", height=300)
            full = {
                "date": str(date.today()),
                "entry": entry
            }
            with open("sample.json", "w") as outfile:
                json.dump(full, outfile)

        elif type == 'video':
            st.write("upload video")
        elif type == 'voice memo':
            st.write("upload voice memo")
        elif type == 'image':
            st.write("upload image")

#--------------calender----------------

#run "pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib"


#from future import print_function
# import streamlit as st
# import pandas as pd
# import numpy as np
# import datetime
# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import buildq
# from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    st.title("Calendar")
    html_string = "<iframe src= 'https://calendar.google.com/calendar/embed?src=joon33103%40gmail.com&ctz=America%2FLos_Angeles' style='border: 0' width='800' height='600' frameborder='0' scrolling='no'></iframe>"
    st.markdown(html_string, unsafe_allow_html=True)
#     events = []
#     creds = None
#     st.header("Calendar")
#     st.markdown("This is the calendar page")
#     def authenticate():
#         creds = None
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     def extract_events():
#         try:
#             service = build('calendar', 'v3', credentials=creds)

#             # Call the Calendar API
#             now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
#             print('Getting the upcoming 10 events')
#             events_result = service.events().list(calendarId='primary', timeMin=now,
#                                                 maxResults=10, singleEvents=True,
#                                                 orderBy='startTime').execute()
#             events = events_result.get('items', [])

#             if not events:
#                 print('No upcoming events found.')
#                 return

#             # Prints the start and name of the next 10 events
#             complete_events = []
#             for event in events:
#                 start = event['start'].get('dateTime', event['start'].get('date'))
#                 descriptive = start + event['summary'] + event["description"]
#                 complete_events.append(descriptive)
#                 # print(start, event['summary'], event["description"])
#                 print(descriptive)
#             return complete_events

#         except HttpError as error:
#             print('An error occurred: %s' % error)
        


# # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#         events = extract_events()
   
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if st.button("Click here to allow access to google calendar"):
#             authenticate()
#             events = extract_events()
        
    
#     st.markdown(events)