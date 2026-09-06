class Delivery:
    def __init__(self, delivery_id, order, driver_name=None):
        self.delivery_id = delivery_id
        self.order = order
        self.driver_name = driver_name
        self.delivery_status = "Awaiting Pickup" # States: Awaiting Pickup, In Transit, Delivered
        self.delivery_address = self.order.customer.get_details()['address']

    def assign_driver(self, driver_name):
        self.driver_name = driver_name
        self.update_tracking("Awaiting Pickup")

    def update_tracking(self, new_status):
        self.delivery_status = new_status
        if new_status == "In Transit":
            self.order.update_status("Out for Delivery")
        elif new_status == "Delivered":
            self.order.update_status("Completed")
            self.order.customer.add_to_history(self.order)

    def get_delivery_info(self):
        return {
            "Delivery ID": self.delivery_id,
            "Order ID": self.order.order_id,
            "Driver": self.driver_name,
            "Destination": self.delivery_address,
            "Status": self.delivery_status
        }