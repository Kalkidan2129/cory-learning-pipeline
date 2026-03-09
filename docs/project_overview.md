# Cory Campaign Intelligence System — Project Overview

---

## Background

Cory is an automated digital outreach worker that contacts potential customers using voice calls, SMS, and email.

While outreach volume was high, the campaign was producing very few bookings. The team did not have clear visibility into why outreach attempts were failing or where leads were dropping off in the conversion process.

Without structured analytics, it was difficult to determine whether the issue was related to timing, channel selection, customer targeting, or conversation quality.

---

## Project Objective

The objective of this project is to build a complete analytics and machine learning system that helps the team understand and optimize Cory's outreach performance.

The system is designed to:

- Measure outreach performance across the full campaign funnel
- Identify where leads drop off in the outreach process
- Diagnose channel, timing, and data quality issues
- Predict which outreach attempts are most likely to produce positive customer intent
- Extract insights from call transcripts to understand common objections

---

## System Architecture

The Cory Campaign Intelligence System is built using multiple analytics layers that transform raw campaign activity into actionable insights.


Campaign Activity Data
↓
SQL Data Modeling (Bronze → Silver → Gold)
↓
Funnel Measurement Framework
↓
Power BI Performance Dashboard
↓
Python Learning Pipeline
↓
Machine Learning Propensity Model
↓
Transcript Objection Analysis
↓
Operational Automation


Each layer adds structure and intelligence to the system, enabling deeper analysis and decision-making.

---

## Data Layers

### Bronze Layer
The Bronze layer inventories raw campaign data tables and documents their structure, relationships, and data quality characteristics.

Key tables include:

- campaign_activities
- campaign_enrollments
- contacts

---

### Silver Layer

The Silver layer standardizes and cleans the raw data.

This layer:

- normalizes keys
- standardizes timestamps
- resolves contact identities
- prepares conformed views for downstream analytics

Key views include:

- `sv_attempt_events_conformed`
- `sv_enrollments_conformed`
- `sv_contacts_conformed`

---

### Gold Layer

The Gold layer provides analytics-ready datasets used for reporting and modeling.

Key views:

- `vw_attempt_ml` — attempt-level dataset
- `vw_enrollment_summary` — enrollment-level summary dataset

These views power both the dashboard and the machine learning pipeline.

---

## Funnel Measurement Framework

The project defines a structured outreach funnel to measure campaign effectiveness.

The funnel stages include:

1. **Reached** – The customer was successfully contacted.
2. **Engaged** – The customer responded or interacted.
3. **Positive Intent** – The customer showed interest in the offer.
4. **Booked Proxy** – The interaction resulted in a booking signal.

This funnel allows the team to identify exactly where prospects drop off during outreach.

---

## Power BI Dashboard

A multi-page dashboard was developed to monitor campaign performance.

Dashboard pages include:

### Funnel Overview
Shows how enrollments progress through the outreach funnel.

### Channel Performance
Analyzes engagement and intent rates across voice, SMS, and email channels.

### Timing Heatmap
Identifies the best outreach times based on day-of-week and hour-of-day performance.

### Quality & Suppression
Tracks opt-outs, wrong numbers, and language barriers.

### Vertical / Persona Insights
Evaluates performance across industries and audience segments.

---

## Python Learning Pipeline

A Python pipeline was developed to automate campaign diagnostics.

The pipeline performs the following tasks:

1. Extracts campaign data from SQL Gold views
2. Validates data integrity (null checks, duplicate detection, extract parity)
3. Exports reproducible parquet datasets
4. Generates campaign performance diagnostics

The pipeline can be executed with one command:


python -m src.run_pipeline --start YYYY-MM-DD --end YYYY-MM-DD


Or via one-click execution:


run_cory_pipeline.bat


---

## Machine Learning Model

A baseline logistic regression model was developed to predict the probability that an outreach attempt will generate positive customer intent.

Key details:

- Dataset: 2018 attempts
- Positive intent rate: 1.49%
- Group split by enrollment_id to prevent data leakage
- One-hot encoding for categorical features

### Model Performance

Baseline positive rate: **1.49%**

Top 10% scored attempts: **10.4%**

Lift: **~7x improvement over baseline**

This allows the team to prioritize outreach efforts toward high-probability prospects.

---

## Transcript Objection Analysis

To understand why outreach attempts fail, call transcripts were analyzed using natural language processing.

Steps included:

1. Transcript extraction and filtering
2. Text cleaning and de-identification
3. TF-IDF feature generation
4. KMeans clustering
5. Rule-based objection tagging

### Identified Objection Categories

- Intro Pitch
- Intro Smalltalk
- Busy / Callback
- Not Interested
- Gatekeeper / Wrong Person
- Pricing Concern
- Payment Processing Objection

This converts qualitative conversation feedback into measurable insights.

---

## Operational Automation

The system was operationalized using a Python automation pipeline.

Execution can be performed using a one-click script:


run_cory_pipeline.bat


This script:

- runs the full pipeline
- validates data quality
- generates updated diagnostics reports
- produces reproducible data snapshots

---

## Business Impact

The Cory Campaign Intelligence System enables the team to:

- identify funnel breakdown points
- understand why outreach attempts fail
- optimize outreach timing
- improve channel strategy
- prioritize high-probability prospects
- understand customer objections at scale

This transforms the outreach process from guesswork into a **data-driven optimization system**.

---

## Project Status

The system now provides an end-to-end campaign intelligence workflow:


Campaign Data
↓
SQL Analytics Layer
↓
Funnel Measurement
↓
Power BI Dashboard
↓
Automated Diagnostics
↓
Predictive Targeting Model
↓
Transcript Objection Insights
↓
Operational Automation


The project is fully implemented and ready to support ongoing campaign monitoring and optimization.

---