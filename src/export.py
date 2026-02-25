# export.py

import os


def export_parquet(df_attempt, df_enrollment):
    os.makedirs("output/data", exist_ok=True)

    df_attempt.to_parquet("output/data/attempt_raw.parquet", index=False)
    df_enrollment.to_parquet("output/data/enrollment_raw.parquet", index=False)

    print("Parquet files exported.")
