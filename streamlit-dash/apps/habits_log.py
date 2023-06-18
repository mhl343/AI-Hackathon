import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def app():
    habits_data = pd.read_csv("data/habits-data.csv")
    st.header("today's habits:")
    today = habits_data.iloc[-1].tolist()
    filtered = [list(habits_data)[i] for i in range(len(list(habits_data))) if today[i]][1:]
    for h in filtered:
        st.write(f"\U00002B50 {h}")

    st.header("top 3 habits maintained!")
    only_habits = habits_data.drop('date', axis=1)
    habits_sum = only_habits.sum()
    habit_props = only_habits.sum() / len(only_habits)
    habit_props = habit_props.sort_values(ascending=False)
    st.write("you are most on track for the following habits!")
    st.write(f"\U0001F60A {habit_props.index[0]}, {habit_props.index[1]}, {habit_props.index[2]} \U0001F60A")

    fig = make_subplots(rows=1, 
                        cols=3,
                        specs=[[{"type": "pie"}, {"type": "pie"}, {"type": "pie"}]],
                        subplot_titles=(habit_props.index[0], habit_props.index[1], habit_props.index[2]))

    fig.add_trace(go.Pie(labels=['checked','unchecked'],
                          values=[habits_sum.iloc[0],len(only_habits)-habits_sum.iloc[0]],
                          hole=0.7,
                          textinfo='none',
                          marker_colors=['rgb(50,64,145)','rgb(240,240,240)'],
                          showlegend=False,
                          ),row=1, col=1),
    
    fig.add_trace(go.Pie(labels=['checked','unchecked'],
                          values=[habits_sum.iloc[1],len(only_habits)-habit_props.iloc[1]],
                          hole=0.7,
                          textinfo='none',
                          marker_colors=['rgb(113,209,145)','rgb(240,240,240)'],
                          showlegend=False,
                          ),row=1, col=2),
        
    fig.add_trace(go.Pie(labels=['checked','unchecked'],
                          values=[habits_sum.iloc[2],len(only_habits)-habits_sum.iloc[2]],
                          hole=0.7,
                          textinfo='none',
                          marker_colors=['rgb(210,50,45)','rgb(240,240,240)'],
                          showlegend=False,
                          ),row=1, col=3)


    fig.add_annotation(x=0.1, y=0.5, text=str(round(habit_props.iloc[0]*100, 2))+"%", showarrow=False)
    fig.add_annotation(x=0.5, y=0.5, text=str(round(habit_props.iloc[1]*100, 2))+"%", showarrow=False)
    fig.add_annotation(x=0.9, y=0.5, text=str(round(habit_props.iloc[2]*100, 2))+"%", showarrow=False)
    
    st.plotly_chart(fig, use_container_width=True)

    st.header("habits log")
    st.write("here you can see all of the data that you have entered into the habit tracker!")
    st.write("(press the \"date\" title to arrange the column in ascending or descending order)")
    st.data_editor(habits_data)
