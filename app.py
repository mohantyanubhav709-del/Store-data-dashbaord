import streamlit as st
import pandas as pd

df = pd.read_csv("store.csv", encoding='latin1')
df.columns = df.columns.str.strip()
import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("store.csv", encoding='latin1')

# Title
st.title("📊 Store Data Dashboard")

# Key Metrics
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", round(df["Sales"].sum(), 2))
col2.metric("Total Profit", round(df["Profit"].sum(), 2))
col3.metric("Total Orders", df.shape[0])

# Sales by Region
st.subheader("Sales by Region")
region_sales = df.groupby("Region")["Sales"].sum()
st.bar_chart(region_sales)

# Sales by Segment
st.subheader("Sales by Segment")
segment_sales = df.groupby("Customer Segment")["Sales"].sum()
st.bar_chart(segment_sales)
