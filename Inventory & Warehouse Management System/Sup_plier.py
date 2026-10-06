class Supplier:

    def __init__(self, supplier_id, supplier_name, phone_no, email):

        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.phone = phone_no
        self.email = email

    def display_supplier_info(self):

        print("----- SUPPLIER DETAILS ------")
        print("Supplier Id:", self.supplier_id)
        print("Supplier Name:", self.supplier_name)
        print("Phone No:", self.phone)
        print("Email:", self.email)
        print("----------------------------------")


class Supplier_Manager:

    def __init__(self):

        self.suppliers = {}

    # ==================================================
    # ADD SUPPLIER
    # ==================================================

    def add_Suppliers(self):

        print("\n========== ADD SUPPLIER ==========")

        # Supplier ID
        supplier_id = input("Enter the supplier id: ").strip()

        if not supplier_id:
            print("Supplier ID cannot be empty!")
            return

        if supplier_id in self.suppliers:
            print("Supplier id already exists!")
            return

        # Supplier Name
        supplier_name = input("Enter the name: ").strip()

        if not supplier_name:
            print("Supplier Name cannot be empty!")
            return

        # Phone Number
        phone = input("Enter the mobile no: ").strip()

        if not phone:
            print("Phone number cannot be empty!")
            return

        if not phone.isdigit():
            print("Phone number must contain only digits!")
            return

        if len(phone) != 10:
            print("Phone number must contain 10 digits!")
            return

        # Email
        email = input("Enter the mail_id: ").strip()

        if not email:
            print("Email cannot be empty!")
            return

        if "@" not in email or "." not in email:
            print("Please enter a valid email!")
            return

        # Create Supplier Object
        supplier = Supplier(
            supplier_id,
            supplier_name,
            phone,
            email
        )

        # Store Supplier
        self.suppliers[supplier_id] = supplier

        print("\nSupplier added successfully!")

    # ==================================================
    # VIEW SUPPLIER
    # ==================================================

    def view_supplier(self):

        if not self.suppliers:

            print("Supplier does not exist!")
            return

        print("\n========= SUPPLIERS =========")

        for supplier in self.suppliers.values():

            supplier.display_supplier_info()

    # ==================================================
    # SEARCH SUPPLIER
    # ==================================================

    def search_supplier(self):

        supplier_id = input("Enter Supplier ID: ").strip()

        if not supplier_id:
            print("Supplier ID cannot be empty!")
            return

        if supplier_id in self.suppliers:

            print("Supplier Found!")

            self.suppliers[supplier_id].display_supplier_info()

        else:

            print("Supplier not found!")

