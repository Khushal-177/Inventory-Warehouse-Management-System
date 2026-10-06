# Inventory & Warehouse Management System

A Python-based **Inventory and Warehouse Management System** built using Object-Oriented Programming (OOP) principles. This modular application helps businesses efficiently track products, manage suppliers, record purchases and sales, and generate detailed analytical reports.

## 🚀 Features

- **Product Management**: Add, view, search, and manage inventory stock levels with automated low-stock and out-of-stock alerts.
- **Supplier Management**: Maintain supplier profiles with validation for contact details and emails.
- **Purchase Management**: Record purchase orders, track supplier restocking, and automatically update product quantities.
- **Sales Management**: Process customer sales, validate real-time stock availability, and calculate revenues.
- **Reports & Analytics**: Generate comprehensive reports including overall inventory overviews, financial summaries, profit margins, and top-performing products.

## 📂 Project Structure

```text
Inventory-Warehouse-Management-System/
│
├── main.py              # Main entry point and menu controller
├── Pro_duct.py          # Product and ProductManager classes
├── Sup_plier.py         # Supplier and Supplier_Manager classes
├── Pur_chase.py         # Purchase and PurchaseManager classes
├── sale.py              # Sale class
├── sales_manager.py     # SalesManager class
└── reports.py           # ReportManager class and analytics