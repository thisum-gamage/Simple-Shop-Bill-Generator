# 🛒 Simple Shop Bill Generator

A lightweight Python application designed to streamline the billing process for small shops or personal use. This tool takes user inputs for multiple items, calculates totals, applies dynamic discounts, and generates a formatted summary.

## ✨ Key Features

* **Multi-Item Entry :** Utilizes Python lists to store and process multiple items in a single transaction.
* **Smart Discount Logic :**
    * **15% Discount** for bills exceeding Rs. 10,000.
    * **10% Discount** for bills exceeding Rs. 5,000.
* **Live Date & Time :** Integrated with the `datetime` module to provide a real-time timestamp on every bill.
* **Professional Formatting :** Outputs a clean, tabular view of items, quantities, and prices using string formatting.
