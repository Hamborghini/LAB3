class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []  # List of dictionaries: {"item": MenuItem, "quantity": int}
        self.status = "Pending" # States: Pending, Confirmed, Preparing, Out for Delivery, Completed
        self.total_amount = 0.0

    def add_item(self, menu_item, quantity=1):
        if menu_item.is_available:
            self.items.append({"item": menu_item, "quantity": quantity})
            self.calculate_total()
        else:
            raise ValueError(f"{menu_item.name} is currently out of stock.")

    def remove_item(self, item_id):
        self.items = [i for i in self.items if i["item"].item_id != item_id]
        self.calculate_total()

    def calculate_total(self):
        self.total_amount = sum(i["item"].price * i["quantity"] for i in self.items)

    def update_status(self, new_status):
        self.status = new_status

    def generate_receipt(self):
        receipt = f"Order ID: {self.order_id}\nCustomer: {self.customer.get_details()['name']}\n"
        for i in self.items:
            receipt += f"{i['quantity']}x {i['item'].name} - ${i['item'].price * i['quantity']:.2f}\n"
        receipt += f"Total: ${self.total_amount:.2f}\nStatus: {self.status}"
        return receipt