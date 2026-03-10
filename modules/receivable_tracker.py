import streamlit as st
import sqlite3

def app():

    st.title("Accounts Receivable Tracker")

    customer_name = st.text_input("Enter Customer Name")

    if st.button("Check Payment Status"):

        conn = sqlite3.connect("data/receivable.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM receivables WHERE customer=?", (customer_name,))
        result = cursor.fetchone()

        if result:
            st.success("Customer Record Found")

            st.write("Customer:", result[0])
            st.write("Invoice Amount:", result[1])
            st.write("Due Date:", result[2])
            st.write("Payment Status:", result[3])

        else:
            st.error("Customer not found")

        conn.close()