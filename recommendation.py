import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("data.csv")

# Combine important features
movies['combined_features'] = (
    movies['genre'] + ' ' +
    movies['description']
)

# Convert text data into numerical vectors
vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(
    movies['combined_features']
)

# Calculate similarity matrix
similarity = cosine_similarity(feature_vectors)


def recommend(movie_name):

    movie_name = movie_name.lower()

    # Find matching movie
    matching_movies = movies[
        movies['title'].str.lower().str.contains(movie_name)
    ]

    if matching_movies.empty:
        return []

    movie_index = matching_movies.index[0]

    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    sorted_movies = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for movie in sorted_movies[1:11]:

        index = movie[0]

        recommendations.append({
            'title': movies.iloc[index]['title'],
            'genre': movies.iloc[index]['genre'],
            'rating': movies.iloc[index]['rating'],
            'description': movies.iloc[index]['description'],
            'similarity_score': round(movie[1] * 100, 2)
        })

    return recommendations