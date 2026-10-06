from Pro_duct import ProductManager
from Pur_chase import PurchaseManager
from Sup_plier import Supplier_Manager
from sales_manager import SalesManager
from reports import ReportManager


# ==============================
# MANAGERS
# ==============================

product_manager = ProductManager()

supplier_manager = Supplier_Manager()

purchase_manager = PurchaseManager(
    product_manager,
    supplier_manager
)

sales_manager = SalesManager(
    product_manager
)

report_manager = ReportManager(
    product_manager,
    purchase_manager,
    sales_manager,
    supplier_manager
)


# ==============================
# MAIN MENU
# ==============================

while True:

    print("\n" + "=" * 50)
    print("       INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Product Management")
    print("2. Supplier Management")
    print("3. Purchase Management")
    print("4. Sales Management")
    print("5. Reports & Analytics")
    print("6. Exit")

    print("=" * 50)

    choice = input("Enter your choice: ")


    # ==============================
    # PRODUCT MANAGEMENT
    # ==============================

    if choice == "1":

        while True:

            print("\n===== PRODUCT MANAGEMENT =====")

            print("1. Add Product")
            print("2. View Products")
            print("3. Search Product")
            print("4. Stock In")
            print("5. Stock Out")
            print("6. Low Stock Products")
            print("7. Back to Main Menu")

            product_choice = input("Enter your choice: ")


            if product_choice == "1":

                product_manager.add_product()


            elif product_choice == "2":

                product_manager.view_products()


            elif product_choice == "3":

                product_manager.search_product()


            elif product_choice == "4":

                product_manager.stock_in()


            elif product_choice == "5":

                product_manager.stock_out()


            elif product_choice == "6":

                product_manager.low_stock_products()


            elif product_choice == "7":

                break


            else:

                print("Invalid Choice!")


    # ==============================
    # SUPPLIER MANAGEMENT
    # ==============================

    elif choice == "2":

        while True:

            print("\n===== SUPPLIER MANAGEMENT =====")

            print("1. Add Supplier")
            print("2. View Suppliers")
            print("3. Search Supplier")
            print("4. Back to Main Menu")

            supplier_choice = input("Enter your choice: ")


            if supplier_choice == "1":

                supplier_manager.add_Suppliers()


            elif supplier_choice == "2":

                supplier_manager.view_supplier()


            elif supplier_choice == "3":

                supplier_manager.search_supplier()


            elif supplier_choice == "4":

                break


            else:

                print("Invalid Choice!")


    # ==============================
    # PURCHASE MANAGEMENT
    # ==============================

    elif choice == "3":

        while True:

            print("\n===== PURCHASE MANAGEMENT =====")

            print("1. Add Purchase")
            print("2. View Purchases")
            print("3. Back to Main Menu")

            purchase_choice = input("Enter your choice: ")


            if purchase_choice == "1":

                purchase_manager.create_purchase()


            elif purchase_choice == "2":

                purchase_manager.view_purchases()


            elif purchase_choice == "3":

                break


            else:

                print("Invalid Choice!")


    # ==============================
    # SALES MANAGEMENT
    # ==============================

    elif choice == "4":

        while True:

            print("\n===== SALES MANAGEMENT =====")

            print("1. Create Sale")
            print("2. View Sales")
            print("3. Search Sale")
            print("4. Back to Main Menu")

            sales_choice = input("Enter your choice: ")


            if sales_choice == "1":

                sales_manager.create_sale()


            elif sales_choice == "2":

                sales_manager.view_sales()


            elif sales_choice == "3":

                sales_manager.search_sale()


            elif sales_choice == "4":

                break


            else:

                print("Invalid Choice!")


    # ==============================
    # REPORTS & ANALYTICS
    # ==============================

    elif choice == "5":

        while True:

            print("\n===== REPORTS & ANALYTICS =====")

            print("1. Overall Report")
            print("2. Product Report")
            print("3. Purchase Report")
            print("4. Sales Report")
            print("5. Supplier Report")
            print("6. Stock Report")
            print("7. Back to Main Menu")

            report_choice = input("Enter your choice: ")


            if report_choice == "1":

                report_manager.overall_report()


            elif report_choice == "2":

                report_manager.product_report()


            elif report_choice == "3":

                report_manager.purchase_report()


            elif report_choice == "4":

                report_manager.sales_report()


            elif report_choice == "5":

                report_manager.supplier_report()


            elif report_choice == "6":

                report_manager.stock_report()


            elif report_choice == "7":

                break


            else:

                print("Invalid Choice!")


    # ==============================
    # EXIT
    # ==============================

    elif choice == "6":

        print("\nInventory Management System Closed!")
        break


    # ==============================
    # INVALID MAIN MENU CHOICE
    # ==============================

    else:

        print("Invalid Choice!")

