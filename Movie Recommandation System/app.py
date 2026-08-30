import streamlit as st
import pickle
import joblib

st.title('Movie Recommendation System')

# Load movie data
with open("movies.pickle", 'rb') as m:
    movies = pickle.load(m)

# Load similarity matrix
similarities = joblib.load("simlarty.joblib")


def recommend(name_movie):

    # Find movie index
    movie_index = movies[
        movies['title'].str.lower() == name_movie.lower()
    ].index[0]

    # Get similarity scores
    distances = similarities[movie_index]

    # Sort movies based on similarity
    recommendations = sorted(
        enumerate(distances),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    # Get top 5 movies
    for i in recommendations[1:6]:
        recommended_movies.append(
            movies.iloc[i[0]]['title']
        )

    return recommended_movies


# Movie names for selectbox
movie_names = movies['title'].values

name_movie = st.selectbox(
    "Enter the Movie Name",
    movie_names
)

if st.button("Recommend"):

    recommended_movies = recommend(name_movie)

    st.write("### Recommended Movies")

    for movie in recommended_movies:
        st.write(movie)