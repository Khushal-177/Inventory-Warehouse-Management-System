class Purchase:

    def __init__(
        self,
        purchase_id,
        supplier_id,
        product_id,
        quantity,
        purchase_price,
        purchase_date
    ):

        self.purchase_id = purchase_id
        self.supplier_id = supplier_id
        self.product_id = product_id
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.purchase_date = purchase_date

        self.total_amount = quantity * purchase_price


    def display_purchase_info(self):

        print("----- PURCHASE DETAILS ------")
        print("Purchase Id:", self.purchase_id)
        print("Supplier Id:", self.supplier_id)
        print("Product Id:", self.product_id)
        print("Quantity:", self.quantity)
        print("Purchase Price:", self.purchase_price)
        print("Purchase Date:", self.purchase_date)
        print("Total Amount:", self.total_amount)
        print("----------------------------------")


class PurchaseManager:

    def __init__(self, product_manager, supplier_manager):

        self.purchases = []
        self.product_manager = product_manager
        self.supplier_manager = supplier_manager


    def create_purchase(self):

        print("\n========== ADD PURCHASE ==========")

        # Purchase ID
        purchase_id = input("Enter Purchase Id: ")


        # Check duplicate Purchase ID
        for purchase in self.purchases:

            if purchase.purchase_id == purchase_id:

                print("Purchase ID already exists!")
                return


        # Supplier ID
        supplier_id = input("Enter Supplier Id: ")


        # Supplier validation
        if supplier_id not in self.supplier_manager.suppliers:

            print("Supplier not found!")
            print("Purchase cancelled.")

            return


        # Product ID
        product_id = input("Enter Product Id: ")


        # Product validation
        if product_id not in self.product_manager.products:

            print("Product not found!")
            print("Purchase cancelled.")

            return


        # Quantity
        try:

            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:

                print("Quantity must be greater than 0.")
                return

        except ValueError:

            print("Please enter a valid quantity!")
            return


        # Purchase Price
        try:

            purchase_price = float(
                input("Enter Purchase Price: ")
            )

            if purchase_price <= 0:

                print("Purchase price must be greater than 0.")
                return

        except ValueError:

            print("Please enter a valid purchase price!")
            return


        # Purchase Date
        purchase_date = input("Enter Purchase Date: ")


        # Get Product Object
        product = self.product_manager.products[product_id]


        # Store Previous Stock
        old_stock = product.quantity


        # Increase Product Stock
        product.quantity += quantity


        # Store New Stock
        new_stock = product.quantity


        # Create Purchase Object
        purchase = Purchase(
            purchase_id,
            supplier_id,
            product_id,
            quantity,
            purchase_price,
            purchase_date
        )


        # Add Purchase to List
        self.purchases.append(purchase)


        # Success Message
        print("\n===== PURCHASE SUCCESSFUL =====")

        print("Purchase ID:", purchase.purchase_id)
        print("Product:", product.product_name)
        print("Previous Stock:", old_stock)
        print("Purchased Quantity:", quantity)
        print("Current Stock:", new_stock)
        print("Purchase Price:", purchase_price)
        print("Total Amount:", purchase.total_amount)

        print("===============================")


    def view_purchases(self):

        if not self.purchases:

            print("\nNo purchase records found!")
            return


        print("\n" + "=" * 120)
        print("                         PURCHASE RECORDS")
        print("=" * 120)


        print(
            f"{'Purchase ID':<15}"
            f"{'Supplier ID':<15}"
            f"{'Product ID':<15}"
            f"{'Quantity':<10}"
            f"{'Price':<15}"
            f"{'Total':<15}"
            f"{'Purchase Date':<20}"
        )


        print("-" * 120)


        for purchase in self.purchases:

            print(
                f"{purchase.purchase_id:<15}"
                f"{purchase.supplier_id:<15}"
                f"{purchase.product_id:<15}"
                f"{purchase.quantity:<10}"
                f"{purchase.purchase_price:<15.2f}"
                f"{purchase.total_amount:<15.2f}"
                f"{purchase.purchase_date:<20}"
            )


        print("=" * 120)