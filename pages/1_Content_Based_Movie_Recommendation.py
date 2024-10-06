import streamlit as st

import streamlit as st
import time
import numpy as np
import pandas as pd
import gzip

st.set_page_config(page_title="Movie Recommendation ", page_icon="📈")
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

@st.cache_data(persist="disk")
def load_model():
    movies = pd.read_csv('models/content_based_movie_recommendation/movies.csv')
    with gzip.open('models/content_based_movie_recommendation/similarity.npy.gz', 'rb') as f:
        similarity = np.load(f, allow_pickle=True)
    return movies, similarity

def recommend(movie_name):
    l_movies, l_similarity = load_model()
    movie_index = l_movies[l_movies['title'] == movie_name].index[0]
    distances = l_similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    l =[]
    for i in movies_list:
        l.append(l_movies.iloc[i[0]].title)
    return l

def create_select_box():
    progress_bar.progress(10)
    status_text.text("%i%% Complete" % 10)
    movies, _ = load_model()
    progress_bar.progress(25)
    status_text.text("%i%% Complete" % 25)
    selected_movie = st.selectbox(options=movies.title, label="Select a movie and get similar recommendation.")
    progress_bar.progress(75)
    status_text.text("%i%% Complete" % 75)
    st.write("We suggest these movies, which are similar the one you selected: ", selected_movie)
    for index, movie in enumerate(recommend(selected_movie)):
        st.write(str(index+1), ": ", movie)
    progress_bar.progress(100)
    status_text.text("%i%% Complete" % 100)
    progress_bar.empty()




st.markdown("# Movie Recommendation using Content-based Filtering")
st.markdown("-------------")
st.sidebar.header("Movie Recommendation using Content-based Filtering")

st.write(
    """
    This demo illustrates a Movie Recommendation system build using content-based filtering. 
    The demo uses the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
    
    Project Source: [MovieRecommendationSystem-ContentBased](https://github.com/adarshtri/MovieRecommendationSystem-ContentBased/tree/main)
    
    You can find the details on the methodology used in building the recommendation model in the GitHub repository.
    """
)

create_select_box()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
