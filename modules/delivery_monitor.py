import streamlit as st
import sqlite3

def app():

    st.title("Delivery Status Monitoring System")

    order_id = st.text_input("Enter Order Number")

    if st.button("Check Delivery Status"):

        conn = sqlite3.connect("data/delivery.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM deliveries WHERE order_id=?", (order_id,))
        result = cursor.fetchone()

        if result:
            st.success("Delivery Details Found")

            st.write("Order Number:", result[0])
            st.write("Customer:", result[1])
            st.write("Delivery Date:", result[2])
            st.write("Delivery Status:", result[3])

        else:
            st.error("Order not found")

        conn.close()