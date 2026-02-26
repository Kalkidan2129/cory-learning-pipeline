import pandas as pd
import joblib

df = pd.read_parquet("output/data/features_preattempt.parquet")
model = joblib.load("output/model.joblib")

target = "is_positive_intent"

X = df.drop(columns=[target])
y = df[target]

X_scoring = X.drop(columns=["enrollment_id"])

df["score"] = model.predict_proba(X_scoring)[:, 1]

# Create deciles
df["decile"] = pd.qcut(df["score"], 10, labels=False)

lift_table = df.groupby("decile").agg(
    attempts=("score", "count"),
    positive_rate=(target, "mean")
).sort_index(ascending=False)

overall_rate = df[target].mean()
lift_table["lift"] = lift_table["positive_rate"] / overall_rate

print("\nOverall Positive Rate:", overall_rate)
print("\nLift Table:")
print(lift_table)