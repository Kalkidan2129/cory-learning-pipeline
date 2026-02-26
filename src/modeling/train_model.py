import pandas as pd
import joblib

from sklearn.model_selection import GroupShuffleSplit
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score


def train_model():

    # --------------------------------------------------
    # Load data
    # --------------------------------------------------
    df = pd.read_parquet("output/data/features_preattempt.parquet")

    target = "is_positive_intent"

    # Basic sanity check
    print("Dataset size:", len(df))
    print("Positive rate:", df[target].mean())

    X = df.drop(columns=[target])
    y = df[target]

    # --------------------------------------------------
    # Leakage assertion
    # --------------------------------------------------
    forbidden_cols = [
        "outcome_norm",
        "call_duration_sec",
        "transcript",
        "is_booked_proxy"
    ]

    for col in forbidden_cols:
        assert col not in X.columns, f"Leakage detected: {col}"

    print("Leakage test passed.")

    # --------------------------------------------------
    # Group split by enrollment_id
    # --------------------------------------------------
    groups = df["enrollment_id"]

    gss = GroupShuffleSplit(test_size=0.2, random_state=42)
    train_idx, test_idx = next(gss.split(X, y, groups))

    X_train, X_test = X.iloc[train_idx].copy(), X.iloc[test_idx].copy()
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    # Verify no enrollment_id leakage
    train_ids = set(X_train["enrollment_id"])
    test_ids = set(X_test["enrollment_id"])
    assert train_ids.isdisjoint(test_ids), "Group leakage detected!"

    print("Group split validation passed.")

    # Remove enrollment_id from features
    X_train = X_train.drop(columns=["enrollment_id"])
    X_test = X_test.drop(columns=["enrollment_id"])

    # --------------------------------------------------
    # Feature definitions
    # --------------------------------------------------
    categorical_cols = [
        "channel",
        "local_dow",
        "prior_attempt_outcome_norm"
    ]

    numeric_cols = [
        "local_hour",
        "attempt_sequence_number",
        "attempts_total_for_enrollment",
        "days_since_last_attempt"
    ]

    # --------------------------------------------------
    # Preprocessing
    # --------------------------------------------------
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numeric_cols),
        ]
    )

    # Important for imbalanced dataset
    model = LogisticRegression(
        max_iter=1000,
        random_state=42,
        class_weight="balanced"
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    # --------------------------------------------------
    # Train model
    # --------------------------------------------------
    pipeline.fit(X_train, y_train)

    y_proba = pipeline.predict_proba(X_test)[:, 1]
    roc = roc_auc_score(y_test, y_proba)

    print(f"ROC AUC: {roc:.4f}")

    # --------------------------------------------------
    # Stability test
    # --------------------------------------------------
    pipeline2 = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", LogisticRegression(
                max_iter=1000,
                random_state=42,
                class_weight="balanced"
            )),
        ]
    )

    pipeline2.fit(X_train, y_train)
    y_proba2 = pipeline2.predict_proba(X_test)[:, 1]
    roc2 = roc_auc_score(y_test, y_proba2)

    assert abs(roc - roc2) < 1e-6, "Stability test failed!"
    print("Stability test passed.")

    # --------------------------------------------------
    # Extract feature drivers
    # --------------------------------------------------
    feature_names = pipeline.named_steps["preprocessor"].get_feature_names_out()
    coefficients = pipeline.named_steps["model"].coef_[0]

    coef_df = pd.DataFrame({
        "feature": feature_names,
        "coefficient": coefficients
    }).sort_values("coefficient", ascending=False)

    print("\nTop Positive Drivers:")
    print(coef_df.head(10))

    print("\nTop Negative Drivers:")
    print(coef_df.tail(10))

    # --------------------------------------------------
    # Save model
    # --------------------------------------------------
    joblib.dump(pipeline, "output/model.joblib")
    print("model.joblib saved.")


if __name__ == "__main__":
    train_model()