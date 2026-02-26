import pandas as pd


def build_features():
    # Load attempt dataset from Story 5 output
    df = pd.read_parquet("output/data/attempt_raw.parquet")

    # -----------------------------
    # Target
    # -----------------------------
    target = "is_positive_intent"

    # -----------------------------
    # Pre-attempt features only
    # -----------------------------
    feature_cols = [
        "enrollment_id",
        "channel",
        "local_hour",
        "local_dow",
        "attempt_sequence_number",
        "attempts_total_for_enrollment",
        "prior_attempt_outcome_norm",
        "days_since_last_attempt",
        target
    ]

    df = df[feature_cols].copy()

    # -----------------------------
    # Basic cleaning
    # -----------------------------
    df["days_since_last_attempt"] = df["days_since_last_attempt"].fillna(0)

    # Save dataset
    df.to_parquet("output/data/features_preattempt.parquet", index=False)

    print("features_preattempt.parquet created.")
    print(f"Rows: {len(df)}")


if __name__ == "__main__":
    build_features()