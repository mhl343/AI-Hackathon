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
    st.write(f"Date: {date.today()}")
    entry = st.text_area("Today's Journal Entry", height=300)
    full = {
                "date": str(date.today()),
                "entry": entry
            }
    
    with open("sample.json", "w") as outfile:
        json.dump(full, outfile)