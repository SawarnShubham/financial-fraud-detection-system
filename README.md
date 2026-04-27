# Financial Fraud Detection & Risk Analytics System

## 🚀 Project Overview

This project analyzes financial transaction behavior using Python, SQL, and Streamlit to detect suspicious transactions, identify high-risk customers, and improve fraud prevention strategies.

The system helps businesses:

- Detect suspicious financial transactions
- Identify fraud behavior patterns
- Monitor high-risk customers
- Analyze fraud trends over time
- Build fraud monitoring dashboards

This project is built using the Credit Card Fraud Detection Dataset and focuses on solving real-world fraud detection problems through data cleaning, exploratory data analysis (EDA), SQL-based business analysis, risk segmentation, and interactive dashboard development.

It is designed as a flagship resume project for Data Analytics and Business Intelligence roles.

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- SQL (SQLite)
- Streamlit
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git & GitHub

---

## 📂 Project Structure

```text
financial-fraud-detection-system/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── creditcard.csv
│   │
│   └── processed/
│       ├── creditcard_cleaned.csv
│       └── fraud_detection.db
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_risk_analysis.ipynb
│
├── screenshots/
│
├── sql/
│   └── queries.sql
│
├── src/
│
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE

## 📥 Dataset Note

Due to GitHub file size limitations, the raw dataset and processed files are not included in this repository.

The following files are excluded:

- `data/raw/creditcard.csv`
- `data/processed/creditcard_cleaned.csv`
- `data/processed/fraud_detection.db`

### How to Run This Project

### Step 1 — Download Dataset

Download the Credit Card Fraud Detection Dataset manually and place it inside:

```text
data/raw/