import streamlit as st
import pandas as pd
from reportlab.pdfgen import canvas
import os
from datetime import datetime

def app():

    st.title("Customer Invoice Generator")

    customer = st.text_input("Customer Name")
    product = st.text_input("Product Name")
    price = st.number_input("Product Price", min_value=0)
    quantity = st.number_input("Quantity", min_value=1)

    if st.button("Generate Invoice"):

        total = price * quantity
        invoice_id = "INV" + datetime.now().strftime("%H%M%S")

        # Save to CSV
        df = pd.read_csv("data/invoice_data.csv")

        new_row = {
            "Invoice_ID": invoice_id,
            "Customer": customer,
            "Product": product,
            "Price": price,
            "Quantity": quantity,
            "Total": total
        }

        df = pd.concat([df, pd.DataFrame([new_row])])
        df.to_csv("data/invoice_data.csv", index=False)

        # Create PDF invoice
        os.makedirs("invoices", exist_ok=True)
        file_path = f"invoices/{invoice_id}.pdf"

        c = canvas.Canvas(file_path)

        c.drawString(100, 750, "INVOICE")
        c.drawString(100, 720, f"Invoice ID: {invoice_id}")
        c.drawString(100, 700, f"Customer: {customer}")
        c.drawString(100, 680, f"Product: {product}")
        c.drawString(100, 660, f"Price: {price}")
        c.drawString(100, 640, f"Quantity: {quantity}")
        c.drawString(100, 620, f"Total Amount: ₹{total}")

        c.save()

        st.success("Invoice Generated Successfully!")
        st.write("Invoice ID:", invoice_id)
        st.write("Total Amount:", total)