# Power BI Integration — Objection Tags

## Overview
Objection tags generated from transcript analysis are integrated into the Power BI campaign dashboard to help explain why outreach attempts fail or succeed.

## Data Source
The objection tags dataset is exported from the NLP pipeline.

Script:
src/nlp/export_tags_csv.py

Output file:
output/data/objection_tags.csv

Fields:
- attempt_id
- objection_tag

## Relationships
The objection tags dataset is linked to the attempts dataset using:

attempts.attempt_id → objection_tags.attempt_id

This allows objection categories to be analyzed across campaign dimensions such as channel, time, and industry.

## Dashboard Page
New page: **Objection Insights**

Visuals included:
- Objection Distribution
- Objections by Channel
- Objections by Time

Slicers:
- Industry
- Channel

## Model Insights Integration
Key drivers from the baseline propensity model are included in the dashboard to highlight factors associated with positive intent.

Examples:
- Voice channel → strong positive predictor
- Thursday outreach → higher engagement
- Email channel → lower success rate

## Data Privacy
No raw transcripts are displayed in the dashboard.  
Only aggregated counts of objection categories are shown to ensure PII safety.

## Refresh Process
1. Run NLP pipeline to regenerate objection tags.
2. Export updated `objection_tags.csv`.
3. Refresh the Power BI dataset to update visuals.