import streamlit as st

from modules import order_tracking
from modules import delivery_monitor
from modules import invoice_generator
from modules import receivable_tracker
from modules import dashboard
from modules import o2c_simulation

st.sidebar.title("Mini O2C ERP System")

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "O2C Process Simulation",
        "Sales Order Tracking",
        "Delivery Monitoring",
        "Invoice Generator",
        "Accounts Receivable",
        "O2C Dashboard"
    ]
)

if menu == "O2C Process Simulation":
    o2c_simulation.app()

elif menu == "Sales Order Tracking":
    order_tracking.app()

elif menu == "Delivery Monitoring":
    delivery_monitor.app()

elif menu == "Invoice Generator":
    invoice_generator.app()

elif menu == "Accounts Receivable":
    receivable_tracker.app()

elif menu == "O2C Dashboard":
    dashboard.app()