import pandas as pd
from sqlalchemy import create_engine
from src.config import CONNECTION_STRING


def extract_transcripts(start_date=None, end_date=None):

    engine = create_engine(CONNECTION_STRING)

    query = """
    SELECT
        attempt_id,
        enrollment_id,
        transcript,
        call_duration_sec,
        channel,
        local_dow,
        local_hour,
        outcome_norm,
        is_positive_intent
    FROM vw_attempt_ml
    WHERE transcript IS NOT NULL
      AND call_duration_sec >= 20
    """

    df = pd.read_sql(query, engine)

    print("Transcripts pulled:", len(df))

    df.to_parquet("output/data/transcripts_filtered.parquet", index=False)

    print("Saved to output/data/transcripts_filtered.parquet")


if __name__ == "__main__":
    extract_transcripts()