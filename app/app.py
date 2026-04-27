import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Financial Fraud Detection Dashboard",
    layout="wide"
)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

df = pd.read_csv("data/processed/creditcard_cleaned.csv")

# ---------------------------------------------------
# Sidebar Filters
# ---------------------------------------------------

st.sidebar.header("Dashboard Filters")

# Transaction Type Filter
transaction_type = st.sidebar.selectbox(
    "Select Transaction Type",
    ["All", "Normal Only", "Fraud Only"]
)

# Amount Range Filter
min_amount = int(df['Amount'].min())
max_amount = int(df['Amount'].max())

amount_range = st.sidebar.slider(
    "Select Amount Range",
    min_value=min_amount,
    max_value=max_amount,
    value=(min_amount, max_amount)
)

# Apply Filters
filtered_df = df.copy()

if transaction_type == "Normal Only":
    filtered_df = filtered_df[filtered_df['Class'] == 0]

elif transaction_type == "Fraud Only":
    filtered_df = filtered_df[filtered_df['Class'] == 1]

filtered_df = filtered_df[
    (filtered_df['Amount'] >= amount_range[0]) &
    (filtered_df['Amount'] <= amount_range[1])
]

# ---------------------------------------------------
# KPI Calculations
# ---------------------------------------------------

total_transactions = len(filtered_df)
fraud_transactions = filtered_df['Class'].sum()

if total_transactions > 0:
    fraud_percentage = (fraud_transactions / total_transactions) * 100
else:
    fraud_percentage = 0

if fraud_transactions > 0:
    avg_fraud_amount = filtered_df[
        filtered_df['Class'] == 1
    ]['Amount'].mean()
else:
    avg_fraud_amount = 0

# ---------------------------------------------------
# Dashboard Title
# ---------------------------------------------------

st.title("Financial Fraud Detection & Risk Analytics System")
st.subheader("Executive Fraud Risk Dashboard")

st.write(
    "Interactive fraud detection dashboard using Python, SQL, "
    "Streamlit, and business intelligence insights."
)

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Transactions", f"{total_transactions:,}")
col2.metric("Fraud Transactions", f"{fraud_transactions:,}")
col3.metric("Fraud Percentage", f"{fraud_percentage:.4f}%")
col4.metric("Average Fraud Amount", f"Rs.{avg_fraud_amount:.2f}")

# ---------------------------------------------------
# Class Distribution Countplot
# ---------------------------------------------------

st.subheader("Class Distribution: Fraud vs Normal")

fig1, ax1 = plt.subplots(figsize=(8, 5))

sns.countplot(
    x='Class',
    data=filtered_df,
    ax=ax1
)

ax1.set_title("Fraud vs Normal Transactions")
ax1.set_xlabel("Class (0 = Normal, 1 = Fraud)")
ax1.set_ylabel("Count of Transactions")

st.pyplot(fig1)

# ---------------------------------------------------
# Boxplot: Amount by Class
# ---------------------------------------------------

st.subheader("Transaction Amount by Class")

fig2, ax2 = plt.subplots(figsize=(8, 5))

sns.boxplot(
    x='Class',
    y='Amount',
    data=filtered_df,
    ax=ax2
)

ax2.set_title("Transaction Amount by Class")
ax2.set_xlabel("Class (0 = Normal, 1 = Fraud)")
ax2.set_ylabel("Transaction Amount")

st.pyplot(fig2)

# ---------------------------------------------------
# Correlation Heatmap
# ---------------------------------------------------

st.subheader("Correlation Heatmap")

fig3, ax3 = plt.subplots(figsize=(14, 8))

correlation = filtered_df.corr()

sns.heatmap(
    correlation,
    cmap="coolwarm",
    ax=ax3
)

ax3.set_title("Feature Correlation Heatmap")

st.pyplot(fig3)

# ---------------------------------------------------
# Executive Business Insights
# ---------------------------------------------------

st.subheader("Executive Fraud Insights")

st.markdown("""
### Key Business Findings

- Fraud transactions represent only **0.1667%** of total transactions,
  showing severe class imbalance.

- Most fraudulent transactions are **low-value transactions**,
  indicating stealth fraud behavior.

- Transaction **Time** is a weak fraud indicator and should not be used
  alone for fraud detection.

- Features like **V17, V14, V12, and V10** are the strongest
  fraud-related indicators.

- High-value transactions are not always fraud; fraud detection should
  focus on behavioral anomalies rather than only transaction amount.

### Strategic Recommendations

- Monitor repeated small unusual transactions,
  not just high-value payments.

- Improve fraud scoring using behavioral features instead of
  rule-based amount thresholds.

- Use anomaly detection + machine learning for stronger
  fraud prevention systems.

- Create real-time fraud alert systems for suspicious
  transaction patterns.
""")