
class Product:

    def __init__(
        self,
        product_id,
        product_name,
        category,
        purchase_price,
        selling_price,
        quantity,
        reorder_level,
        supplier_id
    ):

        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.quantity = quantity
        self.reorder_level = reorder_level
        self.supplier_id = supplier_id


    # ==================================================
    # DISPLAY PRODUCT INFORMATION
    # ==================================================

    def display_product_info(self):

        print("\n----- PRODUCT DETAILS -----")

        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Category:", self.category)
        print("Purchase Price:", self.purchase_price)
        print("Selling Price:", self.selling_price)
        print("Quantity:", self.quantity)
        print("Reorder Level:", self.reorder_level)
        print("Supplier ID:", self.supplier_id)

        print("---------------------------")


class ProductManager:

    def __init__(self):

        self.products = {}


    # ==================================================
    # ADD PRODUCT
    # ==================================================

    def add_product(self):

        print("\n========== ADD PRODUCT ==========")

        product_id = input("Enter Product ID: ").strip()

        if not product_id:

            print("Product ID cannot be empty!")
            return

        if product_id in self.products:

            print("Product ID already exists!")
            return


        product_name = input("Enter Product Name: ").strip()

        if not product_name:

            print("Product Name cannot be empty!")
            return


        category = input("Enter Category: ").strip()

        if not category:

            print("Category cannot be empty!")
            return


        try:

            purchase_price = float(
                input("Enter Purchase Price: ")
            )

            selling_price = float(
                input("Enter Selling Price: ")
            )

            quantity = int(
                input("Enter Quantity: ")
            )

            reorder_level = int(
                input("Enter Reorder Level: ")
            )


            if purchase_price <= 0:

                print("Purchase Price must be greater than 0!")
                return


            if selling_price <= 0:

                print("Selling Price must be greater than 0!")
                return


            if quantity < 0:

                print("Quantity cannot be negative!")
                return


            if reorder_level < 0:

                print("Reorder Level cannot be negative!")
                return


        except ValueError:

            print("Please enter valid numeric values!")
            return


        supplier_id = input(
            "Enter Supplier ID: "
        ).strip()

        if not supplier_id:

            print("Supplier ID cannot be empty!")
            return


        product = Product(
            product_id,
            product_name,
            category,
            purchase_price,
            selling_price,
            quantity,
            reorder_level,
            supplier_id
        )


        self.products[product_id] = product


        print("\nProduct added successfully!")


    # ==================================================
    # VIEW PRODUCTS
    # ==================================================

    def view_products(self):

        if not self.products:

            print("\nNo products available.")
            return


        print("\n" + "=" * 115)

        print(
            f"{'ID':<10}"
            f"{'Product Name':<20}"
            f"{'Category':<18}"
            f"{'Purchase':<12}"
            f"{'Selling':<12}"
            f"{'Quantity':<10}"
            f"{'Reorder':<10}"
            f"{'Supplier':<10}"
        )

        print("=" * 115)


        for product in self.products.values():

            print(
                f"{product.product_id:<10}"
                f"{product.product_name:<20}"
                f"{product.category:<18}"
                f"{product.purchase_price:<12.2f}"
                f"{product.selling_price:<12.2f}"
                f"{product.quantity:<10}"
                f"{product.reorder_level:<10}"
                f"{product.supplier_id:<10}"
            )


        print("=" * 115)


    # ==================================================
    # SEARCH PRODUCT
    # ==================================================

    def search_product(self):

        print("\n========== SEARCH PRODUCT ==========")

        product_id = input(
            "Enter Product ID: "
        ).strip()


        if not product_id:

            print("Product ID cannot be empty!")
            return


        if product_id in self.products:

            print("\nProduct Found!")

            product = self.products[product_id]

            product.display_product_info()

        else:

            print("Product not found!")


    # ==================================================
    # STOCK IN
    # ==================================================

    def stock_in(self):

        print("\n========== STOCK IN ==========")

        product_id = input(
            "Enter Product ID: "
        ).strip()


        if product_id not in self.products:

            print("Product not found!")
            return


        try:

            quantity = int(
                input("Enter Quantity to Add: ")
            )

        except ValueError:

            print("Please enter a valid quantity!")
            return


        if quantity <= 0:

            print("Quantity must be greater than 0!")
            return


        product = self.products[product_id]

        old_stock = product.quantity

        product.quantity += quantity

        new_stock = product.quantity


        print("\n===== STOCK IN SUCCESSFUL =====")

        print("Product:", product.product_name)
        print("Previous Stock:", old_stock)
        print("Added Quantity:", quantity)
        print("Current Stock:", new_stock)

        print("===============================")


    # ==================================================
    # STOCK OUT
    # ==================================================

    def stock_out(self):

        print("\n========== STOCK OUT ==========")

        product_id = input(
            "Enter Product ID: "
        ).strip()


        if product_id not in self.products:

            print("Product not found!")
            return


        try:

            quantity = int(
                input("Enter Quantity to Remove: ")
            )

        except ValueError:

            print("Please enter a valid quantity!")
            return


        if quantity <= 0:

            print("Quantity must be greater than 0!")
            return


        product = self.products[product_id]


        if quantity > product.quantity:

            print("Insufficient stock!")

            print(
                "Available Stock:",
                product.quantity
            )

            print(
                "Requested Quantity:",
                quantity
            )

            return


        old_stock = product.quantity

        product.quantity -= quantity

        new_stock = product.quantity


        print("\n===== STOCK OUT SUCCESSFUL =====")

        print("Product:", product.product_name)
        print("Previous Stock:", old_stock)
        print("Removed Quantity:", quantity)
        print("Current Stock:", new_stock)

        print("================================")


    # ==================================================
    # LOW STOCK PRODUCTS
    # ==================================================

    def low_stock_products(self):

        print("\n========== LOW STOCK PRODUCTS ==========")

        found = False


        for product in self.products.values():

            if product.quantity <= product.reorder_level:

                found = True


                print(
                    "Product ID:",
                    product.product_id
                )

                print(
                    "Product Name:",
                    product.product_name
                )

                print(
                    "Current Stock:",
                    product.quantity
                )

                print(
                    "Reorder Level:",
                    product.reorder_level
                )


                if product.quantity == 0:

                    print("Status: OUT OF STOCK")

                else:

                    print("Status: LOW STOCK")


                print("-" * 45)


        if not found:

            print("No low stock products found.")

