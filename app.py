import streamlit as st
import pickle
import requests

def fetch_poster(movie_titles):
    response = requests.get('https://www.omdbapi.com/?t={}&apikey=5e1ef9ab'.format(movie_titles))
    data = response.json()
    return data['Poster']

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    list_of_movies = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in list_of_movies:
        movie_titles = movies_list.iloc[i[0]].title
        
        recommended_movies.append(movies_list.iloc[i[0]].title)
        #fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_titles))
    return recommended_movies,recommended_movies_posters

movies_list = pickle.load(open('movies.pkl','rb'))
movie_titles = movies_list['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie",
    movie_titles)

if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)

    col1 ,col2 ,col3 , col4, col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

#for running this -> streamlit run app.py