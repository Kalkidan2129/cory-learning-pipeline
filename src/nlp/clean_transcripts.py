import pandas as pd
import re


def clean_text(text):
    if pd.isna(text):
        return ""

    text = text.lower()

    # remove emails
    text = re.sub(r'\S+@\S+', ' ', text)

    # remove phone numbers
    text = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', ' ', text)

    # remove numbers
    text = re.sub(r'\d+', ' ', text)

    # remove special characters
    text = re.sub(r'[^a-z\s]', ' ', text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def clean_transcripts():

    df = pd.read_parquet("output/data/transcripts_filtered.parquet")

    print("Original rows:", len(df))

    df["clean_transcript"] = df["transcript"].apply(clean_text)

    df.to_parquet("output/data/transcripts_cleaned.parquet", index=False)

    print("Cleaned file saved.")
    print("Rows:", len(df))


if __name__ == "__main__":
    clean_transcripts()