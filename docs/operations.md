## Cory Learning Pipeline — Runbook
## Overview

The Cory Learning Pipeline extracts Gold-layer campaign data, validates data quality, exports parquet snapshots, and generates automated diagnostics for weekly performance review.

This pipeline supports the Cory campaign intelligence system by enabling repeatable campaign analysis and operational decision-making.

It transforms raw outreach data into structured analytics outputs that help identify:

Funnel performance

Channel effectiveness

Timing optimization opportunities

Outreach efficiency patterns

## Prerequisites

The following environment requirements must be satisfied before running the pipeline.

  ## Software

Python 3.9+

ODBC Driver 17 for SQL Server

Git (optional but recommended)

  ## Access Requirements

SQL Server access

AgentCory database access

Valid SQL authentication credentials

## What This Pipeline Does

With a single execution, the pipeline performs the following operations.

1️⃣ Data Extraction

The pipeline extracts campaign analytics data from the Gold SQL layer.

Source views:

vw_attempt_ml
vw_enrollment_summary

These views contain normalized campaign activity data used for analytics and modeling.

2️⃣ Data Quality Validation

The pipeline performs automated QA validation checks before producing outputs.

Extract Parity Validation

Ensures SQL row counts match extracted dataframe row counts.

The pipeline fails if counts do not match.

Key Integrity Checks

The pipeline validates:

NULL key rate thresholds

Duplicate primary keys

The pipeline stops execution if any validation fails.

3️⃣ Parquet Dataset Export

Validated data is exported as parquet snapshots for reproducibility.

Output files:

output/data/
    attempt_raw.parquet
    enrollment_raw.parquet

These datasets serve as the foundation for diagnostics and modeling workflows.

4️⃣ Diagnostics Generation

The pipeline automatically generates campaign performance diagnostics.

Generated outputs:

output/reports/
    funnel_by_industry.csv
    channel_effectiveness.csv
    timing_heatmap.csv
    attempt_diminishing_returns.csv

Additional visualization outputs:

channel_effectiveness.png
timing_heatmap.png
attempt_diminishing_returns.png

These outputs support weekly campaign performance reviews.

## Project Structure
cory_learning_pipeline/
│
├── docs/
│    ├── eval_report.md
│    ├── objection_taxonomy.md
│    ├── insights_objections.md
│    ├── operations.md
│    └── refresh_integration_notes.md
│
├── output/
│    ├── data/
│    └── reports/
│
├── src/
│    ├── modeling/
│    ├── nlp/
│    ├── extract.py
│    ├── qa.py
│    ├── export.py
│    ├── diagnostics.py
│    ├── config.py
│    └── run_pipeline.py
│
├── tests/
│
├── run_cory_pipeline.bat
├── pyproject.toml
├── README.md
└── .env
## Setup Instructions
1️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate environment:

venv\Scripts\activate
2️⃣ Install Dependencies
pip install -r requirements.txt
## Configure SQL Connection

Open:

src/config.py

Set the SQL connection string with valid credentials.

Example format:

mssql+pyodbc://username:password@server/AgentCory?driver=ODBC+Driver+17+for+SQL+Server
## How To Run The Pipeline

Run the pipeline from the project root directory.

Example command:

python -m src.run_pipeline --start YYYY-MM-DD --end YYYY-MM-DD

Example execution:

python -m src.run_pipeline --start 2025-11-01 --end 2026-02-01
## Expected Console Output
Starting pipeline...
Extracted XXXX attempts and XXXX enrollments.
Extract parity check passed.
QA checks passed.
Parquet files exported.
Diagnostics report generated.
Pipeline completed successfully.

If any validation fails, the pipeline stops execution and raises an error.

## Automated Pipeline Execution

The pipeline can also be executed using the automation script:

run_cory_pipeline.bat

This script performs the following steps automatically:

Navigates to the project directory

Activates the Python virtual environment

Executes the Cory learning pipeline

Generates updated parquet datasets and diagnostics reports

To run the pipeline using the automation script:

Navigate to the project folder

Double-click:

run_cory_pipeline.bat

The pipeline will execute automatically and display progress in a command window.

Example output:

Starting pipeline...
Extracted XXXX attempts and XXXX enrollments.
Extract parity check passed.
QA checks passed.
Parquet files exported.
Diagnostics report generated.
Pipeline completed successfully.
## Output Artifacts
  ## Data Snapshots
output/data/
    attempt_raw.parquet
    enrollment_raw.parquet

These datasets are used for diagnostics and modeling workflows.

  ## Diagnostics Reports
output/reports/
    funnel_by_industry.csv
    channel_effectiveness.csv
    timing_heatmap.csv
    attempt_diminishing_returns.csv

Visualization outputs:

channel_effectiveness.png
timing_heatmap.png
attempt_diminishing_returns.png
## Reproducibility

Running the pipeline with the same date range produces:

identical row counts

stable parquet datasets

consistent diagnostic outputs

This ensures deterministic and repeatable campaign analytics.

## Operational Use

This pipeline supports recurring campaign performance analysis by identifying:

funnel breakdown points

high-performing industries

effective outreach channels

optimal outreach timing

diminishing returns across repeated attempts

This enables data-driven outreach optimization without manual exploration of raw campaign data.

## Ownership

Owner: Dev-A
System: Cory Campaign Intelligence Platform
Pipeline: Cory Learning Pipeline

## Change Log
Date	Change	Author
2026-02-20	Initial pipeline implementation	Dev-A
2026-03-09	Added automation script and operational documentation	Dev-A
## End of Document