
from sale import Sale


class SalesManager:

    def __init__(self, product_manager):

        self.product_manager = product_manager
        self.sales = []


    # ==========================================
    # CREATE SALE
    # ==========================================

    def create_sale(self):

        print("\n========== CREATE SALE ==========")

        # Sale ID
        sale_id = input("Enter Sale ID: ").strip()

        if not sale_id:
            print("Sale ID cannot be empty!")
            return

        # Duplicate Sale ID Check
        for sale in self.sales:

            if sale.sale_id == sale_id:

                print("Sale ID already exists!")
                return


        # Product ID
        product_id = input("Enter Product ID: ").strip()

        if not product_id:
            print("Product ID cannot be empty!")
            return


        # Product Validation
        if product_id not in self.product_manager.products:

            print("Product not found!")
            return


        product = self.product_manager.products[product_id]


        # Quantity
        try:

            quantity = int(input("Enter Quantity: "))

        except ValueError:

            print("Please enter a valid quantity!")
            return


        if quantity <= 0:

            print("Quantity must be greater than 0!")
            return


        # Stock Validation
        if quantity > product.quantity:

            print("Insufficient stock!")
            print("Available Stock:", product.quantity)
            print("Requested Quantity:", quantity)

            return


        # Selling Price
        selling_price = product.selling_price


        # Store Previous Stock
        old_stock = product.quantity


        # Reduce Stock
        product.quantity -= quantity


        # Store New Stock
        new_stock = product.quantity


        # Create Sale
        sale = Sale(
            sale_id,
            product_id,
            quantity,
            selling_price
        )


        # Store Sale
        self.sales.append(sale)


        # Success Message
        print("\n===== SALE CREATED SUCCESSFULLY =====")

        print("Sale ID:", sale.sale_id)
        print("Product:", product.product_name)
        print("Previous Stock:", old_stock)
        print("Sold Quantity:", quantity)
        print("Selling Price:", selling_price)
        print("Total Amount:", sale.total_amount)
        print("Remaining Stock:", new_stock)

        print("=====================================")


    # ==========================================
    # VIEW SALES
    # ==========================================

    def view_sales(self):

        if not self.sales:

            print("\nNo sales available.")
            return


        print("\n" + "=" * 100)
        print("                         SALES HISTORY")
        print("=" * 100)


        print(
            f"{'Sale ID':<15}"
            f"{'Product ID':<15}"
            f"{'Quantity':<12}"
            f"{'Price':<15}"
            f"{'Total':<15}"
            f"{'Date':<20}"
        )


        print("-" * 100)


        for sale in self.sales:

            print(
                f"{sale.sale_id:<15}"
                f"{sale.product_id:<15}"
                f"{sale.quantity:<12}"
                f"{sale.selling_price:<15.2f}"
                f"{sale.total_amount:<15.2f}"
                f"{sale.sale_date:<20}"
            )


        print("=" * 100)


    # ==========================================
    # SEARCH SALE
    # ==========================================

    def search_sale(self):

        sale_id = input("Enter Sale ID: ").strip()


        if not sale_id:

            print("Sale ID cannot be empty!")
            return


        for sale in self.sales:

            if sale.sale_id == sale_id:

                print("\nSale Found!")

                sale.display_sale_info()

                return


        print("Sale not found!")

