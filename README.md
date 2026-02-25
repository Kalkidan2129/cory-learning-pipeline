# Cory Learning Pipeline

Automated data extraction, QA validation, parquet snapshot generation, and campaign diagnostics for Cory.

## What This Project Does

- Extracts Gold-layer campaign data
- Validates data integrity
- Exports parquet snapshots
- Generates automated diagnostics
- Supports weekly optimization decisions

## Project Structure

docs/        → Documentation  
src/         → Source code  
tests/       → Test files  
output/      → Generated artifacts (ignored in Git)

## Setup

Create virtual environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -e .

## Run Pipeline

python -m src.run_pipeline --start YYYY-MM-DD --end YYYY-MM-DD