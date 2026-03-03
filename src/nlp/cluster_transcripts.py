import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def cluster_transcripts():

    df = pd.read_parquet("output/data/transcripts_cleaned.parquet")

    print("Rows:", len(df))

    # -----------------------------
    # TF-IDF Vectorization
    # -----------------------------
    vectorizer = TfidfVectorizer(
        max_features=1000,
        stop_words="english",
        ngram_range=(1, 2)
    )

    X = vectorizer.fit_transform(df["clean_transcript"])

    print("TF-IDF matrix shape:", X.shape)

    # -----------------------------
    # KMeans Clustering
    # -----------------------------
    n_clusters = 7

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["cluster"] = kmeans.fit_predict(X)

    # -----------------------------
    # Inspect Top Words Per Cluster
    # -----------------------------
    terms = vectorizer.get_feature_names_out()
    centroids = kmeans.cluster_centers_

    print("\nTop words per cluster:\n")

    for i in range(n_clusters):
        center = centroids[i]
        top_indices = center.argsort()[-10:][::-1]
        top_terms = [terms[ind] for ind in top_indices]

        print(f"Cluster {i}:")
        print(", ".join(top_terms))
        print("-" * 50)

    df.to_parquet("output/data/transcripts_clustered.parquet", index=False)

    print("Clustered file saved.")


if __name__ == "__main__":
    cluster_transcripts()