import streamlit as st
import pandas as pd

def app():

    st.title("O2C Business Dashboard")

    df = pd.read_csv("data/invoice_data.csv")

    total_orders = len(df)
    total_revenue = df["Total"].sum()

    st.metric("Total Orders", total_orders)
    st.metric("Total Revenue", total_revenue)

    st.bar_chart(df["Total"])