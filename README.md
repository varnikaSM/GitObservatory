# GitObservatory 🔭

**GitObservatory** is an end-to-end GitHub Repository Analytics platform that enables users to compare GitHub repositories using a modern Data Engineering architecture built on **Azure Databricks**, **Delta Lake**, and **Streamlit**.

The platform ingests repository metadata and activity from the GitHub REST API, processes it through a Medallion Architecture (Bronze → Silver → Gold), and presents interactive repository health analytics through a Streamlit dashboard.

---

## Features

- Compare any two public GitHub repositories
- Configurable analysis windows (1 Month, 2 Months, Quarter, 6 Months, 1 Year, 2 Years)
- Azure Databricks Workflow orchestration
- Medallion Architecture (Bronze, Silver, Gold)
- Repository Health Score calculation
- Repository grading and health status
- Pull Request analytics
- Issue analytics
- Contributor analytics
- GitHub Actions workflow analytics
- Interactive Streamlit dashboard

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

## Future Enhancements

- AI-powered repository health explanations
- Automated repository improvement recommendations
- Historical repository trend analysis
- Multi-repository comparison
- GitHub organization analytics

---

## Author

**Varnika S. M.**

Built as a Data Engineering portfolio project demonstrating Azure Databricks, Delta Lake, GitHub REST APIs, workflow orchestration, and interactive analytics.
