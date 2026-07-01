# Databricks Pipeline

This folder contains the complete Azure Databricks implementation of GitObservatory.

## Notebook Execution Order

1. 00_Repository_Input
2. 01_Bronze_Ingestion
3. 02_Silver_Transformation
4. 03_Gold_Analytics

## Medallion Architecture

Bronze
- Raw GitHub API data

Silver
- Cleaned and transformed analytics tables

Gold
- Business metrics and repository comparison tables

## Workflow

The Databricks Job orchestrates the complete ingestion and transformation pipeline before the Streamlit dashboard retrieves Gold-layer analytics.
