import streamlit as st
import sqlite3

def app():

    st.title("Sales Order Tracking System")

    order_id = st.text_input("Enter Order ID")

    if st.button("Track Order"):

        conn = sqlite3.connect("data/orders.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM orders WHERE order_id=?", (order_id,))
        result = cursor.fetchone()

        if result:
            st.success("Order Found")

            st.write("Order ID:", result[0])
            st.write("Customer:", result[1])
            st.write("Status:", result[2])

        else:
            st.error("Order not found")

        conn.close()