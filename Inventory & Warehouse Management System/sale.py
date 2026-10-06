from datetime import datetime

class Sale:
    def __init__(self,sale_id,product_id,quantity,selling_price):

        self.sale_id = sale_id
        self.product_id = product_id
        self.quantity = quantity
        self.selling_price = selling_price
        self.total_amount = quantity * selling_price
        self.sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def display_sale_info(self):

        print("----- SALE DETAILS -----")
        print("Sale ID:", self.sale_id)
        print("Product ID:", self.product_id)
        print("Quantity:", self.quantity)
        print("Selling Price:", self.selling_price)
        print("Total Amount:", self.total_amount)
        print("Sale Date:", self.sale_date)
