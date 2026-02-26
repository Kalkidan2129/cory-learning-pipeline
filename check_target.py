# check_target.py
import pandas as pd

df = pd.read_parquet("output/data/features_preattempt.parquet")

print("Positive rate:", df["is_positive_intent"].mean())
print(df["is_positive_intent"].value_counts())