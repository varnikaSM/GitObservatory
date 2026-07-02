# 🔭 GitObservatory

## GitHub Repository Analytics & Comparison Platform

GitObservatory is an end-to-end Data Engineering project that compares GitHub repositories using real engineering metrics rather than popularity alone.

The project automatically ingests GitHub repository metadata, pull requests, issues, contributors, workflow executions, and code review information through the GitHub REST API. The data is processed using the Medallion Architecture (Bronze → Silver → Gold) on Azure Databricks before being presented through an interactive Streamlit dashboard.

The platform enables users to compare open-source repositories based on engineering health, development activity, workflow reliability, and community engagement.

---
---

## Repository Health Score

GitObservatory computes a **Repository Health Score (0–100)** using multiple engineering and community metrics.

The score incorporates:

- Community popularity
  - Stars
  - Forks

- Development activity
  - Active contributors
  - Pull Requests
  - Merge activity

- Repository maintenance
  - Issue management
  - Issue closure rate

- CI/CD reliability
  - GitHub Actions workflow success

The Health Score is translated into:

| Health Score | Grade | Status |
|--------------|-------|------------------|
| 90–100 | A+ | Excellent |
| 80–89 | A | Very Healthy |
| 70–79 | B | Healthy |
| 60–69 | C | Moderate |
| <60 | D | Needs Improvement |

---

# Architecture

```
GitHub REST API
        │
        ▼
Azure Databricks Workflow
        │
        ▼
Bronze Layer
Raw GitHub Data
        │
        ▼
Silver Layer
Cleaned & Standardized Data
        │
        ▼
Gold Layer
Repository Analytics
        │
        ▼
SQL Warehouse
        │
        ▼
Streamlit Dashboard
```

---

## Medallion Architecture

### Bronze Layer

Raw ingestion from GitHub REST APIs.

Includes:

- Repository Metadata
- Pull Requests
- Issues
- Contributors
- Pull Request Reviews
- GitHub Actions Workflow Runs

---

### Silver Layer

Data cleansing and standardization.

Examples:

- Timestamp conversion
- Duplicate removal
- Repository enrichment
- Merge duration calculation
- Issue resolution calculation
- Review classification

---

### Gold Layer

Business-ready analytics.

Examples:

- Repository Health Score
- Merge Rate
- Issue Closure Rate
- Contributor Metrics
- Workflow Success Rate
- Repository Recommendation

---

## Dashboard

The Streamlit dashboard provides:

- Repository Overview
- Repository Health
- Pull Request Analytics
- Issue Analytics
- Contributor Analytics
- Workflow Analytics
- Radar Chart Comparison
- Repository Insights
- Detailed Repository Comparison

---

## Technology Stack

| Layer | Technology |
|--------|------------|
| Programming Language | Python |
| Data Engineering | Azure Databricks |
| Storage | Delta Lake |
| Processing | Apache Spark |
| API | GitHub REST API |
| Dashboard | Streamlit |
| Visualization | Plotly |
| Version Control | Git & GitHub |

---

## Repository Structure

```
GitObservatory/

├── app.py
├── assets/
├── dashboard/
├── utils/
├── databricks/
│   ├── notebooks/
│   ├── workflow/
│   └── dbc/
├── requirements.txt
└── README.md
```

---

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/<username>/GitObservatory.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file containing:

```
DATABRICKS_HOST=<your-host>

DATABRICKS_TOKEN=<your-token>

SQL_WAREHOUSE_ID=<warehouse-id>

JOB_ID=<workflow-job-id>
```

### 4. Start Streamlit

```bash
streamlit run app.py
```

---
---

# Repository Selection

Users simply provide two GitHub repository URLs and choose an analysis window. Once submitted, the application automatically triggers the Azure Databricks pipeline.

<img src="ui1.png" width="900">

---

# Pipeline Execution

After validation, an Azure Databricks Workflow orchestrates the complete Medallion pipeline from data ingestion to dashboard generation.

<img src="ui2.png" width="900">

---

# Repository Overview

The dashboard presents a side-by-side comparison of both repositories, including:

- Repository Health Score
- Repository Grade
- Repository Status
- Stars
- Forks
- Watchers

This provides a quick executive summary before exploring detailed analytics.

<img src="ui3.png" width="900">

---

# Key Performance Indicators

GitObservatory computes engineering KPIs including:

- Repository Health Score
- Merge Rate
- Issue Closure Rate
- Workflow Success Rate
- Approval Rate
- Average Contributor Activity

These metrics are calculated from the processed Gold layer.

<img src="ui4.png" width="900">

---

# Visual Analytics

Interactive Plotly visualizations compare repository performance across multiple engineering dimensions.

Available charts include:

- Repository Health Score
- Pull Request Analytics
- Issue Closure Rate
- Contributor Activity
- Workflow Success Rate
- Overall Repository Radar Comparison

<img src="ui5.png" width="900">

---

# Repository Insights

The dashboard automatically generates repository recommendations and engineering observations based on the computed analytics.

Examples include:

- Repository recommendation
- Merge efficiency comparison
- CI/CD reliability
- Community activity
- Issue management effectiveness

<img src="ui7.png" width="900">

---
# Azure Databricks Workflow

The complete ETL process is orchestrated using Azure Databricks Workflows.

<img src="workflow1.png" width="900">

---

# Workflow Monitoring

Each notebook is executed sequentially, ensuring successful completion of Bronze, Silver, and Gold transformations.

<img src="workflow2.png" width="900">

---

# Successful Pipeline Execution

Once all tasks complete successfully, the Gold analytics tables are refreshed and made available to the dashboard.

<img src="workflow3.png" width="900">

---

# Unity Catalog

Unity Catalog manages all Bronze, Silver, and Gold Delta tables while providing centralized governance for the project.

<img src="catalog.png" width="900">

---

# Gold Layer Analytics

The Gold warehouse stores repository-level KPIs and comparison metrics that power the Streamlit dashboard.

Metrics include:

- Repository Health Score
- Overall Repository Score
- Repository Grade
- Repository Status
- Merge Rate
- Issue Closure Rate
- Workflow Success Rate
- Contributor Metrics

<img src="warehouse.png" width="900">

---

# Key Features

- Compare any two public GitHub repositories
- Automated Azure Databricks Workflow
- Medallion Architecture implementation
- Bronze, Silver and Gold Delta tables
- Repository Health Score
- Repository Grade Classification
- Interactive Plotly dashboards
- Repository comparison insights
- Engineering KPI computation
- Streamlit frontend

---

# Future Enhancements

- AI-powered repository recommendations using Large Language Models
- Historical repository trend analysis
- Multi-repository comparison
- Repository risk prediction
- Natural language repository explanations
- GitHub Actions integration
- Time-series engineering analytics

---

# Author

**Varnika Sasi Magesh**

GitObservatory was developed as a hands-on Data Engineering project to apply Azure Databricks, Delta Lake, Medallion Architecture, PySpark, GitHub REST API integration, workflow orchestration, and interactive analytics in a real-world engineering use case.
