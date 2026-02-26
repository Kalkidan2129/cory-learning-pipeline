Baseline Propensity Model — Positive Intent
1. Objective

Build a baseline classifier to predict is_positive_intent using only information available before each attempt.
The goal is to enable smarter prioritization and reduce low-value outreach.

2. Dataset Overview

Total attempts: 2018

Positive intent attempts: 30

Overall positive rate: 1.49%

Train/Test split: 80/20

Split method: Group split by enrollment_id (prevents same-person leakage)

The dataset is highly imbalanced (1.49% positive rate), requiring proper validation controls.

3. Validation Controls

The following safeguards were implemented:

✅ Leakage test: No post-attempt fields used as features

✅ Group split validation: No enrollment_id appears in both train and test

✅ Stability test: Model trained twice with same seed produced identical ROC AUC

✅ Class imbalance handled using class_weight="balanced"

All validation checks passed successfully.

4. Model Details

Model: Logistic Regression

Random seed: 42

Preprocessing:

One-hot encoding for categorical features

Numeric passthrough for continuous features

Target: is_positive_intent

Performance

ROC AUC: 0.9559

Interpretation:

The model demonstrates strong ability to separate positive intent vs non-positive attempts despite severe class imbalance.

5. Key Feature Drivers
Strong Positive Drivers

Voice channel (channel_voice)

Prior email sent

Prior completed call

Thursday timing

SMS follow-up exposure

Interpretation:

Voice-based and multi-touch sequences significantly increase probability of positive intent.

Strong Negative Drivers

Email-only channel

Voicemail outcomes

Monday timing

Long gaps between attempts (days_since_last_attempt)

High total attempts per enrollment

Interpretation:

Passive channels and delayed follow-ups reduce likelihood of positive intent.

6. Lift Analysis

Overall positive rate: 1.49%

Top 10% Scored Attempts (Decile 9)

Positive rate: 10.4%

Lift: 6.99x above baseline

Bottom 50% Scored Attempts

Observed positive rate: 0%

Interpretation:

The model strongly concentrates positive intent in the top decile.
Targeting only high-scoring attempts would dramatically increase efficiency.

7. Campaign Recommendations

Prioritize top 30–40% of scored attempts for outreach.

Reduce email-only outreach strategies.

Increase emphasis on voice channel for high-score segments.

Avoid extended gaps between attempts.

Limit excessive attempts per enrollment (diminishing returns observed).

8. How to Use Model Scores

Score range: 0–1 (higher = higher probability of positive intent)

Suggested operational use:

Rank attempts weekly by score

Prioritize top deciles for agent routing

Reduce outreach to bottom deciles

Can be integrated into weekly campaign planning pipeline.

Conclusion

This baseline model establishes a methodologically sound and reproducible framework for predicting positive intent.

The lift analysis demonstrates clear opportunity to:

Reduce wasted outreach

Improve agent efficiency

Increase conversion concentration

Story 6 objectives have been successfully completed.