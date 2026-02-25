# qa.py

from src.config import MAX_NULL_RATE


def run_qa(df_attempt, df_enrollment):
    # Null checks
    if df_attempt["attempt_id"].isnull().mean() > MAX_NULL_RATE:
        raise Exception("Too many NULL attempt_id values")

    if df_enrollment["enrollment_id"].isnull().mean() > MAX_NULL_RATE:
        raise Exception("Too many NULL enrollment_id values")

    # Duplicate checks
    if df_attempt["attempt_id"].duplicated().any():
        raise Exception("Duplicate attempt_id found")

    if df_enrollment["enrollment_id"].duplicated().any():
        raise Exception("Duplicate enrollment_id found")

    print("QA checks passed.")
