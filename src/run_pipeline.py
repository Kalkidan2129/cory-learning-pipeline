# run_pipeline.py

import argparse
from src.extract import extract_data
from src.qa import run_qa
from src.export import export_parquet
from src.diagnostics import generate_diagnostics 


def main(start_date, end_date):
    print("Starting pipeline...")

    df_attempt, df_enrollment, sql_attempt_count, sql_enrollment_count = extract_data(start_date, end_date)

    print(f"Extracted {len(df_attempt)} attempts and {len(df_enrollment)} enrollments.")

    # ----------------------------------------
    # Extract Parity Validation
    # ----------------------------------------

    if len(df_attempt) != sql_attempt_count:
        raise Exception("Attempt row count mismatch between SQL and extracted dataframe.")

    if len(df_enrollment) != sql_enrollment_count:
        raise Exception("Enrollment row count mismatch between SQL and extracted dataframe.")

    print("Extract parity check passed.")

    run_qa(df_attempt, df_enrollment)

    export_parquet(df_attempt, df_enrollment)

    generate_diagnostics(df_attempt, df_enrollment)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    args = parser.parse_args()

    main(args.start, args.end)
