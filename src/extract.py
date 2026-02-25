# extract.py

import pandas as pd
from sqlalchemy import create_engine, text
from src.config import CONNECTION_STRING


def extract_data(start_date, end_date):
    engine = create_engine(CONNECTION_STRING)

    attempt_query = f"""
    SELECT *
    FROM vw_attempt_ml
    WHERE event_time_utc >= '{start_date}'
      AND event_time_utc < '{end_date}'
    """

    enrollment_query = f"""
    SELECT *
    FROM vw_enrollment_summary
    WHERE started_at >= '{start_date}'
      AND started_at < '{end_date}'
    """

    attempt_count_query = f"""
    SELECT COUNT(*) AS cnt
    FROM vw_attempt_ml
    WHERE event_time_utc >= '{start_date}'
      AND event_time_utc < '{end_date}'
    """

    enrollment_count_query = f"""
    SELECT COUNT(*) AS cnt
    FROM vw_enrollment_summary
    WHERE started_at >= '{start_date}'
      AND started_at < '{end_date}'
    """

    df_attempt = pd.read_sql(attempt_query, engine)
    df_enrollment = pd.read_sql(enrollment_query, engine)

    sql_attempt_count = pd.read_sql(attempt_count_query, engine)["cnt"][0]
    sql_enrollment_count = pd.read_sql(enrollment_count_query, engine)["cnt"][0]

    return df_attempt, df_enrollment, sql_attempt_count, sql_enrollment_count
