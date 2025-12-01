import streamlit as st

import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

with open("movies.pkl", "rb") as f:
    movies = pickle.load(f)
movie=pd.DataFrame(movies)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)


# movies_list=pickle.load(open('movies.pkl','rb'))
# movies_list=movies_list['title'].values



st.title("movies recommender systems")


selected_movie_name=st.selectbox("Search Movies",
                    movie['title'].values)

if st.button("recommend movies"):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
