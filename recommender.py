import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    """Load the career skills dataset."""
    return pd.read_csv("raw_skills.csv")


def recommend_jobs(user_skills, top_n=3):
    """
    Recommend career roles using
    TF-IDF and Cosine Similarity.
    """

    # Load career dataset
    df = load_data()

    # Make sure the Skills column has no empty values
    df["Skills"] = df["Skills"].fillna("")

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )

    # Convert career skills into TF-IDF vectors
    job_vectors = vectorizer.fit_transform(
        df["Skills"]
    )

    # Convert user's skills into a TF-IDF vector
    user_vector = vectorizer.transform(
        [user_skills]
    )

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(
        user_vector,
        job_vectors
    ).flatten()

    # Add similarity score to dataframe
    df["Similarity_Score"] = similarity_scores

    # Sort careers from highest to lowest similarity
    df = df.sort_values(
        by="Similarity_Score",
        ascending=False
    )

    # Return Top N careers
    return df.head(top_n)