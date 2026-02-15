import pandas as pd
import streamlit as st
import pickle
import requests
import pandas as pd


def fetch_poster(movie_id):
    # Replace with your actual TMDB API Key
    api_key = "39c95498c75b51fb28fbd866bf89d3d5"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    response = requests.get(url)
    data = response.json()

    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

@st.cache_resource
def load_model():
    movies_dict = pickle.load(open('movies_dict.pkl' , 'rb'))
    movies_df = pd.DataFrame(movies_dict)
    similarity_matrix = pickle.load(open('similarity.pkl' , 'rb'))
    return movies_df , similarity_matrix
movies , similarity = load_model()

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)) , reverse = True , key = lambda x:x[1])[1:6]

    recommended_movies = []
    recommend_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies , recommend_movies_poster

st.title("Movie Recommendation Systems")
selected_movies_name = st.selectbox("Select a movie",movies['title'].values)

if st.button('Recommend'):
    with st.spinner('Fetching recommendations and posters...'):
        names , posters = recommend(selected_movies_name)

        cols = st.columns(5)

        for i , col in enumerate(cols):
            with col:
                st.text(names[i])
                st.image(posters[i])
