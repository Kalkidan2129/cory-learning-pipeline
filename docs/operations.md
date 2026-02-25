# Cory Learning Pipeline — Runbook

---

## Overview

The Cory Learning Pipeline extracts Gold-layer campaign data, validates data quality, exports parquet snapshots, and generates automated diagnostics for weekly performance review.

This pipeline is non-ML and designed to support repeatable campaign learning and operational decision-making.

---

## Prerequisites

- Python 3.9+
- ODBC Driver 17 for SQL Server installed
- SQL access to the AgentCory database
- Valid SQL authentication credentials

---

## What This Pipeline Does

With one command, the pipeline:

### 1️⃣ Extracts Data From:
- `vw_attempt_ml`
- `vw_enrollment_summary`

### 2️⃣ Validates:
- Null key rates
- Duplicate keys
- Extract parity (SQL row counts vs extracted dataframe row counts)

### 3️⃣ Exports Parquet Snapshots:
- `attempt_raw.parquet`
- `enrollment_raw.parquet`

### 4️⃣ Generates Diagnostics:
- Funnel conversion by industry
- Channel effectiveness
- Timing heatmap
- Attempt diminishing returns

---

## Project Structure

cory_learning_pipeline/
│
├── extract.py
├── qa.py
├── export.py
├── diagnostics.py
├── run_pipeline.py
├── config.py
├── requirements.txt
├── output/
│ ├── data/
│ └── reports/
└── runbook.md


---

## Setup Instructions

### 1️⃣ (Optional but Recommended) Create Virtual Environment

python -m venv venv
venv\Scripts\activate


### 2️⃣ Install Dependencies

pip install -r requirements.txt


---

## Configure SQL Connection

Open `config.py` and set:

- SQL username
- SQL password
- Server
- Database

Example format:

mssql+pyodbc://username:password@server/AgentCory?driver=ODBC+Driver+17+for+SQL+Server


---

## How To Run

From the project root:

python run_pipeline.py --start YYYY-MM-DD --end YYYY-MM-DD


Example:

python run_pipeline.py --start 2025-11-01 --end 2026-02-01


---

## Expected Console Output

Starting pipeline...
Extracted XXXX attempts and XXXX enrollments.
Extract parity check passed.
QA checks passed.
Parquet files exported.
Diagnostics report generated.
Pipeline completed successfully.


If any validation fails, the pipeline will stop and raise an error.

---

## Output Artifacts

### Data Snapshots

output/data/
├── attempt_raw.parquet
└── enrollment_raw.parquet


### Diagnostics Reports

output/reports/
├── funnel_by_industry.csv
├── channel_effectiveness.csv
├── timing_heatmap.csv
├── attempt_diminishing_returns.csv
├── channel_effectiveness.png
├── timing_heatmap.png
└── attempt_diminishing_returns.png


---

## Validation Controls

### Extract Parity
Ensures SQL row counts match extracted dataframe row counts.  
Pipeline fails if mismatch is detected.

### QA Checks
Pipeline fails if:
- `attempt_id` null rate exceeds configured threshold
- `enrollment_id` null rate exceeds configured threshold
- Duplicate keys are detected

---

## Reproducibility

Re-running the same date range produces:
- Identical row counts
- Stable parquet outputs
- Consistent diagnostics results

This ensures deterministic and repeatable analytics outputs.

---

## Operational Use

This pipeline supports weekly campaign review by identifying:

- Funnel breakdown points
- High-performing industries
- Effective channels
- Optimal timing windows
- Diminishing returns by attempt number

It enables data-driven optimization decisions without requiring manual Power BI interaction.

---

## Status

Story 5 is complete when:

- Code committed
- Parquet datasets generated
- Diagnostics generated
- Runbook included
- Example output attached

---

## Ownership

Owner: Dev-A  
Story: Story 5 — Python Light (Extract + QA + Parquet + Diagnostics)

---

## Change Log

| Date       | Change                    | Author |
|------------|---------------------------|--------|
| 2026-02-20 | Initial implementation    | Dev-A |

---

## End of Document