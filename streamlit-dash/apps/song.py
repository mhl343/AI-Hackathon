import streamlit as st
import pandas as pd
import hume
from pprint import pprint
import numpy as np
import nltk
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn
nltk.download('wordnet')
nltk.download('sentiwordnet')

def app():
    st.title("let's pick a song for you!")
    #day = st.text_input('describe how you are feeling in one word:')
    #tokens is a list
    #tokens = day.split()

    def calculate_correlation(word1, word2):
        synsets1 = wordnet.synsets(word1)
        synsets2 = wordnet.synsets(word2)

        # Calculate the correlation score
        correlation = 0
        for synset1 in synsets1:
            for synset2 in synsets2:
                correlation += swn.senti_synset(synset1.name()).pos_score() * swn.senti_synset(synset2.name()).pos_score()
                correlation += swn.senti_synset(synset1.name()).neg_score() * swn.senti_synset(synset2.name()).neg_score()

        return correlation

    # def calculate_correlation(word1, word2):
    #     synsets1 = wordnet.synsets(word1)
    #     synsets2 = wordnet.synsets(word2)

    #     # Calculate the correlation score
    #     for synset1 in synsets1:
    #         w1_pos = swn.senti_synset(synset1.name()).pos_score()
    #         w1_neg = swn.senti_synset(synset1.name()).neg_score()
    #         w1_obj = swn.senti_synset(synset1.name()).obj_score()
    #         w1_vec = np.array([w1_pos, w1_neg, w1_obj])
    #         w1_vec_std = (w1_vec - np.sum(w1_vec)) / np.std(w1_vec)
    #         for synset2 in synsets2:
    #             w2_pos = swn.senti_synset(synset2.name()).pos_score()
    #             w2_neg = swn.senti_synset(synset2.name()).neg_score()
    #             w2_obj = swn.senti_synset(synset2.name()).obj_score()
    #             w2_vec = np.array([w2_pos, w2_neg, w2_obj])
    #             w2_vec_std = (w2_vec - np.sum(w2_vec)) / np.std(w2_vec)

    #             correlation = np.corrcoef(w1_vec_std, w2_vec_std)[0][1]
    #             if correlation:
    #                 return correlation
    #             else:
    #                 return 0

    def load_data():
        songs = pd.read_csv("data/spotify.csv")
        return songs

    my_word = st.text_input('describe how you are feeling in one word:')
    list_of_features = ["danceability", "energy", "loudness", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo"]
    #list_of_features = ["energy", "loudness", "liveness", "valence", "tempo"]
    songs = load_data()
    columns = songs.columns

    if my_word: 
        correlation_scores = []
        for feature in list_of_features:
            if feature in columns:
                correlation_scores.append(calculate_correlation(my_word, feature))
            else:
                correlation_scores.append(None)

        # Display the correlation scores
        feature_score = {}
        for i, feature in enumerate(list_of_features):
            feature_score[feature] = correlation_scores[i]
            # if correlation_scores[i] is not None:
            #     st.write(f"Correlation between '{my_word}' and '{feature}': {correlation_scores[i]}")
            # else:
            #     st.write(f"'{feature}' not found in the DataFrame.")
        sorted_dict = dict(sorted(feature_score.items(), key=lambda x: x[1], reverse=True))
        top_3_features = ['uri'] + list(sorted_dict.keys())[:3]
        st.markdown("#### your top 3 features that influenced this song choice: ")
        st.markdown("#### " + str(top_3_features[1:4]))
        
        #finding the song 
        new_df = songs[top_3_features]
        new_df['sum'] = new_df.iloc[:, -3:].mean(axis=1)
        sorted_df = new_df.sort_values(by='sum', ascending=False)
        uri = sorted_df.iloc[0, new_df.columns.get_loc('uri')]

        st.header("a song for you based on your mood!")
        spotify_uri_t = uri.split(":")[-1]+'?'
        #spotify_uri_t = '1Ukxccao1BlWrPhYkcXbwZ?'
        #st.write(spotify_uri_t)
        st.write(f'<iframe src="https://open.spotify.com/embed/track/{spotify_uri_t}utm_source=generator" width="500" height="250" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)
        toggle = False

    
    #fiona's stuff
    # st.header("random song")
    # spotify_uri = '1Ukxccao1BlWrPhYkcXbwZ?'
    # st.write(f'<iframe src="https://open.spotify.com/embed/track/{spotify_uri}utm_source=generator" width="500" height="250" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)
    
    #st.header("random picture")
    #st.write(f'<iframe src="https://www.freddieandmillietoys.ie/wp-content/uploads/2022/01/MPSittingTeddyCream33cm-1_540x540.jpg" width="540" height="540" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)

    st.header("picture mood:")
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

    #st.header("all entries")

    #st.header("your journalling analytics")
    #insert hume ai api that takes all data and creates a visualization