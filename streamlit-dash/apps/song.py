import streamlit as st
import pandas as pd
import hume
from pprint import pprint

def app():
    st.title("Let's Pick a Song for You!")
    day = st.text_input('Describe how you are feeling!')

    #def load_data():
    #dfplayers = pd.read_csv("data/deals.csv", index_col=0)
    #return dfplayers
    
    st.header("random song")
    spotify_uri = '1Ukxccao1BlWrPhYkcXbwZ?'
    st.write(f'<iframe src="https://open.spotify.com/embed/track/{spotify_uri}utm_source=generator" width="500" height="250" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)
    
    st.header("random picture")
    st.write(f'<iframe src="https://www.freddieandmillietoys.ie/wp-content/uploads/2022/01/MPSittingTeddyCream33cm-1_540x540.jpg" width="540" height="540" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)

    st.header("today's entry")
    client = hume.HumeBatchClient("ah6Ql98AGK1M58FaJNdSG9QSeAjPUOP1indKn6t6Q7TWTRaL")
    urls = ["https://iep.utm.edu/wp-content/media/hume-bust.jpg"]
    config = hume.models.config.FaceConfig()
    job = client.submit_job(urls, [config])
    details = job.await_complete()
    predictions = job.get_predictions()
    predictions1 = predictions[0]['results']['predictions'][0]['models']['face']['grouped_predictions'][0]['predictions'][0]['emotions']
    #st.write(predictions[0]['results']['predictions'][0]['models']['face']['grouped_predictions'][0]['predictions'][0]['emotions'])
    df = pd.DataFrame.from_records(predictions1)
    #st.write(df)
    edited_df = st.data_editor(df)


    # if not completed yet, then complete here
    # if completed, show hume ai analysis for the day

    st.header("all entries")

    st.header("your journalling analytics")
    #insert hume ai api that takes all data and creates a visualization