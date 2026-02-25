# diagnostics.py

import os
import matplotlib.pyplot as plt
import pandas as pd


def generate_diagnostics(df_attempt, df_enrollment):
    os.makedirs("output/reports", exist_ok=True)

    # ----------------------------------------
    # 1️⃣ Funnel conversion by Industry
    # ----------------------------------------

    if "industry" in df_enrollment.columns:

        industry_summary = (
            df_enrollment
            .groupby("industry")
            .agg(
                total_enrollments=("enrollment_id", "count"),
                intent_rate=("ever_positive_intent", "mean"),
                booked_rate=("ever_booked_proxy", "mean")
            )
            .reset_index()
        )

        industry_summary.to_csv(
            "output/reports/funnel_by_industry.csv",
            index=False
        )

    # ----------------------------------------
    # 2️⃣ Channel Effectiveness
    # ----------------------------------------

    channel_summary = (
        df_attempt
        .groupby("channel")
        .agg(
            attempts=("attempt_id", "count"),
            engagement_rate=("is_engaged", "mean"),
            intent_rate=("is_positive_intent", "mean")
        )
        .reset_index()
    )

    channel_summary.to_csv(
        "output/reports/channel_effectiveness.csv",
        index=False
    )

    plt.figure()
    channel_summary.set_index("channel")["intent_rate"].plot(kind="bar")
    plt.title("Positive Intent Rate by Channel")
    plt.ylabel("Intent Rate")
    plt.tight_layout()
    plt.savefig("output/reports/channel_effectiveness.png")
    plt.close()

    # ----------------------------------------
    # 3️⃣ Timing Heatmap
    # ----------------------------------------

    if "local_hour" in df_attempt.columns and "local_dow" in df_attempt.columns:

        heatmap = (
            df_attempt
            .pivot_table(
                index="local_hour",
                columns="local_dow",
                values="is_positive_intent",
                aggfunc="mean"
            )
        )

        heatmap.to_csv("output/reports/timing_heatmap.csv")

        plt.figure(figsize=(10, 6))
        plt.imshow(heatmap.fillna(0), aspect="auto")
        plt.colorbar(label="Intent Rate")
        plt.title("Intent Rate by Hour and Day")
        plt.ylabel("Local Hour")
        plt.xlabel("Day of Week")
        plt.tight_layout()
        plt.savefig("output/reports/timing_heatmap.png")
        plt.close()

    # ----------------------------------------
    # 4️⃣ Attempt Diminishing Returns
    # ----------------------------------------

    if "attempt_sequence_number" in df_attempt.columns:

        diminishing = (
            df_attempt
            .groupby("attempt_sequence_number")
            .agg(
                attempts=("attempt_id", "count"),
                intent_rate=("is_positive_intent", "mean")
            )
            .reset_index()
        )

        diminishing.to_csv(
            "output/reports/attempt_diminishing_returns.csv",
            index=False
        )

        plt.figure()
        plt.plot(
            diminishing["attempt_sequence_number"],
            diminishing["intent_rate"]
        )
        plt.title("Intent Rate by Attempt Number")
        plt.xlabel("Attempt Sequence")
        plt.ylabel("Intent Rate")
        plt.tight_layout()
        plt.savefig("output/reports/attempt_diminishing_returns.png")
        plt.close()

    print("Diagnostics report generated.")
