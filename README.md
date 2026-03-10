## Overview
**O2C Mini ERP** (Order-to-Cash Enterprise Resource Planning) is a Python-based application designed to manage and track the complete order-to-cash cycle for businesses. It provides modules for **sales order management, delivery tracking, and dashboard analytics**, enabling efficient handling of customer orders and deliveries.

---

## Demo
![O2C Mini ERP Demo](demo.gif)  
*Example of tracking an order and viewing dashboard analytics.*

---

## Features
- **Sales Order Tracking** – Track orders using unique Order IDs.
- **Delivery Monitoring** – Monitor delivery progress and fulfillment status.
- **Dashboard Analytics** – Visual representation of orders and deliveries.
- **Database Integration** – Uses SQLite (`orders.db`, `delivery.db`) for storing data.
- **User-Friendly Interface** – Built with Streamlit for smooth interaction.

---

## Technology Stack
- Python 3.x  
- SQLite  
- Pandas  
- Streamlit  
- Git & GitHub  

---

## Folder Structure
O2C_Mini_ERP/
│
├── app.py                 # Main entry point
├── style.css              # Styles for Streamlit app
├── orders.db              # SQLite database for orders
├── delivery.db            # SQLite database for deliveries
├── demo.gif               # GIF demo of the app
├── modules/
│   ├── order_tracking.py  # Module to track orders
│   ├── delivery_monitor.py# Module to track deliveries
│   └── dashboard.py       # Dashboard module
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies

---

## Installation & Setup
1.**Clone the repository**
git clone 
cd O2C_Mini_ERP https://github.com/sowmyapotharlanka1319-ux/O2C_Mini_ERP.git

2.**Install dependencies**
pip install -r requirements.txt

3.**Run the application**
streamlit run app.py

4.Open the URL displayed in the terminal (usually http://localhost:8501) to access the app.

---

## Usage
Order Tracking – Enter the Order ID to view order details.
Delivery Monitoring – Track delivery status for all orders.
Dashboard – Visualize key metrics and analytics.

## Contribution
Contributions are welcome! Fork the repository, create a branch, and submit a pull request. Ensure all new features or fixes are tested before submitting.

## License
This project is licensed under the MIT License – see the LICENSE file for details.



