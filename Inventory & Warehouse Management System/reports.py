
class ReportManager:

    def __init__(
        self,
        product_manager,
        purchase_manager,
        sales_manager,
        supplier_manager
    ):

        self.product_manager = product_manager
        self.purchase_manager = purchase_manager
        self.sales_manager = sales_manager
        self.supplier_manager = supplier_manager


    # ==========================================
    # INVENTORY OVERVIEW
    # ==========================================

    def inventory_overview(self):

        products = self.product_manager.products
        suppliers = self.supplier_manager.suppliers

        total_products = len(products)
        total_suppliers = len(suppliers)

        total_stock = 0
        inventory_value = 0

        for product in products.values():

            total_stock += product.quantity

            inventory_value += (
                product.quantity *
                product.purchase_price
            )

        in_stock = 0
        low_stock = 0
        out_of_stock = 0

        for product in products.values():

            if product.quantity == 0:

                out_of_stock += 1

            elif product.quantity <= product.reorder_level:

                low_stock += 1

            else:

                in_stock += 1

        return (
            total_products,
            total_suppliers,
            total_stock,
            inventory_value,
            in_stock,
            low_stock,
            out_of_stock
        )


    # ==========================================
    # STOCK SUMMARY
    # ==========================================

    def stock_summary(self):

        products = self.product_manager.products

        print("\n===== STOCK SUMMARY & LOW STOCK ALERTS =====")
        print("-" * 75)

        print(
            f"{'Product ID':<15}"
            f"{'Product Name':<25}"
            f"{'Quantity':<12}"
            f"{'Status':<18}"
        )

        print("-" * 75)

        if not products:

            print("No products available.")
            return

        for product in products.values():

            if product.quantity == 0:

                status = "OUT OF STOCK"

            elif product.quantity <= product.reorder_level:

                status = "LOW STOCK"

            else:

                status = "IN STOCK"

            print(
                f"{str(product.product_id):<15}"
                f"{str(product.product_name):<25}"
                f"{product.quantity:<12}"
                f"{status:<18}"
            )

        print("-" * 75)


    # ==========================================
    # PURCHASE SUMMARY
    # ==========================================

    def purchase_summary(self):

        purchases = self.purchase_manager.purchases

        total_records = len(purchases)
        total_quantity = 0
        total_cost = 0

        for purchase in purchases:

            total_quantity += purchase.quantity
            total_cost += purchase.total_amount

        return (
            total_records,
            total_quantity,
            total_cost
        )


    # ==========================================
    # SALES SUMMARY
    # ==========================================

    def sales_summary(self):

        sales = self.sales_manager.sales

        total_records = len(sales)
        total_quantity = 0
        total_revenue = 0

        for sale in sales:

            total_quantity += sale.quantity
            total_revenue += sale.total_amount

        return (
            total_records,
            total_quantity,
            total_revenue
        )


    # ==========================================
    # PROFIT ANALYSIS
    # ==========================================

    def profit_analysis(
        self,
        total_cost,
        total_revenue
    ):

        profit = total_revenue - total_cost

        if total_revenue > 0:

            profit_margin = (
                profit / total_revenue
            ) * 100

        else:

            profit_margin = 0

        return profit, profit_margin


    # ==========================================
    # TOP PERFORMING PRODUCTS
    # ==========================================

    def top_performing_products(self):

        sales = self.sales_manager.sales

        product_sales = {}

        for sale in sales:

            product_id = sale.product_id

            if product_id in product_sales:

                product_sales[product_id] += sale.quantity

            else:

                product_sales[product_id] = sale.quantity

        sorted_products = sorted(
            product_sales.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return sorted_products[:3]


    # ==========================================
    # SUPPLIER ANALYSIS
    # ==========================================

    def supplier_analysis(self):

        purchases = self.purchase_manager.purchases

        supplier_purchase = {}

        for purchase in purchases:

            supplier_id = purchase.supplier_id

            if supplier_id in supplier_purchase:

                supplier_purchase[supplier_id] += (
                    purchase.total_amount
                )

            else:

                supplier_purchase[supplier_id] = (
                    purchase.total_amount
                )

        if not supplier_purchase:

            return None

        top_supplier = max(
            supplier_purchase,
            key=supplier_purchase.get
        )

        top_amount = supplier_purchase[top_supplier]

        return top_supplier, top_amount


    # ==========================================
    # 1. OVERALL REPORT
    # ==========================================

    def overall_report(self):

        print("\n" + "=" * 75)
        print("             INVENTORY ANALYTICS & REPORTS")
        print("=" * 75)


        # --------------------------------------
        # INVENTORY OVERVIEW
        # --------------------------------------

        (
            total_products,
            total_suppliers,
            total_stock,
            inventory_value,
            in_stock,
            low_stock,
            out_of_stock
        ) = self.inventory_overview()


        print("\n1. INVENTORY OVERVIEW")
        print("-" * 75)

        print("Total Products           :", total_products)
        print("Total Suppliers          :", total_suppliers)
        print("Total Stock Units        :", total_stock)

        print(
            "Total Inventory Value    : ₹{:.2f}".format(
                inventory_value
            )
        )

        print("In Stock Products        :", in_stock)
        print("Low Stock Products       :", low_stock)
        print("Out of Stock Products    :", out_of_stock)


        # --------------------------------------
        # STOCK SUMMARY
        # --------------------------------------

        self.stock_summary()


        # --------------------------------------
        # PURCHASE SUMMARY
        # --------------------------------------

        (
            total_purchase_records,
            total_purchase_quantity,
            total_purchase_cost
        ) = self.purchase_summary()


        print("\n3. PURCHASE SUMMARY")
        print("-" * 75)

        print(
            "Total Purchase Records  :",
            total_purchase_records
        )

        print(
            "Total Items Purchased   :",
            total_purchase_quantity
        )

        print(
            "Total Purchase Cost     : ₹{:.2f}".format(
                total_purchase_cost
            )
        )


        # --------------------------------------
        # SALES SUMMARY
        # --------------------------------------

        (
            total_sales_records,
            total_sold_quantity,
            total_sales_revenue
        ) = self.sales_summary()


        print("\n4. SALES & FINANCIAL SUMMARY")
        print("-" * 75)

        print(
            "Total Sales Records     :",
            total_sales_records
        )

        print(
            "Total Items Sold        :",
            total_sold_quantity
        )

        print(
            "Total Sales Revenue     : ₹{:.2f}".format(
                total_sales_revenue
            )
        )


        # --------------------------------------
        # PROFIT
        # --------------------------------------

        profit, profit_margin = self.profit_analysis(
            total_purchase_cost,
            total_sales_revenue
        )


        print("-" * 75)

        print(
            "Estimated Profit        : ₹{:.2f}".format(
                profit
            )
        )

        print(
            "Profit Margin           : {:.2f}%".format(
                profit_margin
            )
        )


        # --------------------------------------
        # TOP PRODUCTS
        # --------------------------------------

        top_products = self.top_performing_products()


        print("\n5. TOP PERFORMING PRODUCTS")
        print("-" * 75)

        if not top_products:

            print("No sales data available.")

        else:

            print(
                f"{'Rank':<8}"
                f"{'Product':<30}"
                f"{'Units Sold':<15}"
            )

            print("-" * 55)

            for index, (
                product_id,
                quantity
            ) in enumerate(
                top_products,
                start=1
            ):

                product = (
                    self.product_manager.products.get(
                        product_id
                    )
                )

                if product:

                    print(
                        f"{index:<8}"
                        f"{product.product_name:<30}"
                        f"{quantity:<15}"
                    )


        # --------------------------------------
        # SUPPLIER ANALYSIS
        # --------------------------------------

        supplier_result = self.supplier_analysis()


        print("\n6. SUPPLIER ANALYSIS")
        print("-" * 75)

        if supplier_result is None:

            print("No purchase data available.")

        else:

            top_supplier, top_amount = supplier_result

            supplier = (
                self.supplier_manager.suppliers.get(
                    top_supplier
                )
            )

            if supplier:

                print(
                    "Top Supplier             :",
                    supplier.supplier_name
                )

            else:

                print(
                    "Top Supplier             :",
                    top_supplier
                )

            print(
                "Purchase Amount          : ₹{:.2f}".format(
                    top_amount
                )
            )


        # --------------------------------------
        # ATTENTION REQUIRED
        # --------------------------------------

        print("\n7. ATTENTION REQUIRED")
        print("-" * 75)

        print(
            "Low Stock Products       :",
            low_stock
        )

        print(
            "Out of Stock Products    :",
            out_of_stock
        )

        print("\n" + "=" * 75)
        print("                    END OF REPORT")
        print("=" * 75)


    # ==========================================
    # 2. PRODUCT REPORT
    # ==========================================

    def product_report(self):

        products = self.product_manager.products

        print("\n" + "=" * 90)
        print("                    PRODUCT REPORT")
        print("=" * 90)

        if not products:

            print("No products available.")
            return

        print(
            f"{'ID':<12}"
            f"{'Product Name':<25}"
            f"{'Category':<18}"
            f"{'Qty':<10}"
            f"{'Purchase':<15}"
            f"{'Selling':<15}"
        )

        print("-" * 90)

        for product in products.values():

            print(
                f"{str(product.product_id):<12}"
                f"{str(product.product_name):<25}"
                f"{str(product.category):<18}"
                f"{product.quantity:<10}"
                f"₹{product.purchase_price:<14.2f}"
                f"₹{product.selling_price:<14.2f}"
            )

        print("-" * 90)
        print("Total Products:", len(products))


    # ==========================================
    # 3. PURCHASE REPORT
    # ==========================================

    def purchase_report(self):

        purchases = self.purchase_manager.purchases

        print("\n" + "=" * 100)
        print("                    PURCHASE REPORT")
        print("=" * 100)

        if not purchases:

            print("No purchase records available.")
            return

        print(
            f"{'Purchase ID':<15}"
            f"{'Supplier ID':<15}"
            f"{'Product ID':<15}"
            f"{'Quantity':<12}"
            f"{'Price':<12}"
            f"{'Total':<15}"
            f"{'Date':<20}"
        )

        print("-" * 100)

        for purchase in purchases:

            print(
                f"{str(purchase.purchase_id):<15}"
                f"{str(purchase.supplier_id):<15}"
                f"{str(purchase.product_id):<15}"
                f"{purchase.quantity:<12}"
                f"₹{purchase.purchase_price:<11.2f}"
                f"₹{purchase.total_amount:<14.2f}"
                f"{str(purchase.purchase_date):<20}"
            )

        print("-" * 100)

        (
            total_records,
            total_quantity,
            total_cost
        ) = self.purchase_summary()

        print(
            "Total Purchase Records :",
            total_records
        )

        print(
            "Total Items Purchased  :",
            total_quantity
        )

        print(
            "Total Purchase Cost    : ₹{:.2f}".format(
                total_cost
            )
        )


    # ==========================================
    # 4. SALES REPORT
    # ==========================================

    def sales_report(self):

        sales = self.sales_manager.sales

        print("\n" + "=" * 100)
        print("                    SALES REPORT")
        print("=" * 100)

        if not sales:

            print("No sales records available.")
            return

        print(
            f"{'Sale ID':<15}"
            f"{'Product ID':<15}"
            f"{'Quantity':<12}"
            f"{'Price':<12}"
            f"{'Total':<15}"
            f"{'Date':<20}"
        )

        print("-" * 100)

        for sale in sales:

            print(
                f"{str(sale.sale_id):<15}"
                f"{str(sale.product_id):<15}"
                f"{sale.quantity:<12}"
                f"₹{sale.selling_price:<11.2f}"
                f"₹{sale.total_amount:<14.2f}"
                f"{str(sale.sale_date):<20}"
            )

        print("-" * 100)

        (
            total_records,
            total_quantity,
            total_revenue
        ) = self.sales_summary()

        print(
            "Total Sales Records  :",
            total_records
        )

        print(
            "Total Items Sold     :",
            total_quantity
        )

        print(
            "Total Sales Revenue  : ₹{:.2f}".format(
                total_revenue
            )
        )


    # ==========================================
    # 5. SUPPLIER REPORT
    # ==========================================

    def supplier_report(self):

        suppliers = self.supplier_manager.suppliers

        print("\n" + "=" * 90)
        print("                    SUPPLIER REPORT")
        print("=" * 90)

        if not suppliers:

            print("No suppliers available.")
            return

        print(
            f"{'Supplier ID':<15}"
            f"{'Supplier Name':<25}"
            f"{'Phone':<20}"
            f"{'Email':<30}"
        )

        print("-" * 90)

        for supplier in suppliers.values():

            print(
                f"{str(supplier.supplier_id):<15}"
                f"{str(supplier.supplier_name):<25}"
                f"{str(supplier.phone):<20}"
                f"{str(supplier.email):<30}"
            )

        print("-" * 90)
        print("Total Suppliers:", len(suppliers))


    # ==========================================
    # 6. STOCK REPORT
    # ==========================================

    def stock_report(self):

        products = self.product_manager.products

        print("\n" + "=" * 90)
        print("                      STOCK REPORT")
        print("=" * 90)

        if not products:

            print("No products available.")
            return

        print(
            f"{'Product ID':<15}"
            f"{'Product Name':<25}"
            f"{'Quantity':<12}"
            f"{'Reorder Level':<15}"
            f"{'Status':<18}"
        )

        print("-" * 90)

        for product in products.values():

            if product.quantity == 0:

                status = "OUT OF STOCK"

            elif product.quantity <= product.reorder_level:

                status = "LOW STOCK"

            else:

                status = "IN STOCK"

            print(
                f"{str(product.product_id):<15}"
                f"{str(product.product_name):<25}"
                f"{product.quantity:<12}"
                f"{product.reorder_level:<15}"
                f"{status:<18}"
            )

        print("-" * 90)

        (
            total_products,
            total_suppliers,
            total_stock,
            inventory_value,
            in_stock,
            low_stock,
            out_of_stock
        ) = self.inventory_overview()

        print("Total Stock Units     :", total_stock)

        print(
            "Inventory Value       : ₹{:.2f}".format(
                inventory_value
            )
        )

        print("In Stock Products     :", in_stock)
        print("Low Stock Products    :", low_stock)
        print("Out of Stock Products :", out_of_stock)

