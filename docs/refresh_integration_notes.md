# Power BI Integration — Objection Tags

## Overview
Objection tags generated from transcript analysis are integrated into the Power BI campaign dashboard to explain why outreach attempts fail or succeed.

## Data Source
The objection tags dataset is exported from the NLP pipeline:

src/nlp/export_tags_csv.py

Output file:
output/data/objection_tags.csv

Fields:
- attempt_id
- objection_tag

## Integration Steps
1. Load objection_tags.csv into Power BI.
2. Create relationship:
   attempts.attempt_id → objection_tags.attempt_id
3. Use objection_tag as categorical dimension for visualizations.

## Dashboard Page
New page: **Objection Insights**

Visuals included:
- Objection Distribution
- Objections by Channel
- Objections by Time

Slicers:
- Industry
- Channel

## Data Privacy
No raw transcripts are displayed in the dashboard.  
Only aggregated counts of objection categories are shown.

## Refresh Process
1. Run NLP pipeline to regenerate objection tags.
2. Export updated objection_tags.csv.
3. Refresh Power BI dataset.
