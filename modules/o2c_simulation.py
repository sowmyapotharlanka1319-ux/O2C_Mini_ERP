import streamlit as st
import pandas as pd

def app():

    st.title("Order to Cash (O2C) Process Simulation")

    # Load Excel Data
    customers = pd.read_excel("data/customers.xlsx")
    orders = pd.read_excel("data/sales_orders.xlsx")
    deliveries = pd.read_excel("data/deliveries.xlsx")
    invoices = pd.read_excel("data/invoices.xlsx")
    payments = pd.read_excel("data/payments.xlsx")

    st.header("1. Customer Master Creation")
    st.dataframe(customers)

    st.header("2. Sales Order Creation")
    st.dataframe(orders)

    st.header("3. Delivery Processing")
    st.dataframe(deliveries)

    st.header("4. Invoice Generation")
    st.dataframe(invoices)

    st.header("5. Payment Posting")
    st.dataframe(payments)

    # Calculate revenue
    total_revenue = invoices["Amount"].sum()

    st.subheader("Total Revenue")
    st.success(f"₹ {total_revenue}")