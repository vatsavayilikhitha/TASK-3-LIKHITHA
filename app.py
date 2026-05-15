import streamlit as st
from recommendation import recommend

st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 AI Movie Recommendation System")

st.write(
    "Get smart movie recommendations using AI similarity matching"
)

movie_name = st.text_input(
    "Enter a movie name"
)

if st.button("Recommend"):

    recommendations = recommend(movie_name)

    if recommendations:

        st.subheader("Top Recommendations")

        for movie in recommendations:

            st.markdown("---")

            st.write(f"### 🎥 {movie['title']}")
            st.write(f"Genre: {movie['genre']}")
            st.write(f"⭐ Rating: {movie['rating']}")
            st.write(
                f"🔥 Similarity Score: "
                f"{movie['similarity_score']}%"
            )
            st.write(movie['description'])

    else:
        st.error("Movie not found in dataset")