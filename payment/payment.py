class Payment:
    def __init__(self, payment_id, order, amount, payment_method):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.payment_method = payment_method  # e.g., "Credit Card", "Cash", "Digital Wallet"
        self.status = "Pending" # States: Pending, Authorized, Completed, Failed

    def process_payment(self):
        # In a real app, this would integrate with a payment gateway (e.g., Stripe, PayPal)
        if self.amount >= self.order.total_amount:
            self.status = "Completed"
            self.order.update_status("Confirmed")
            return True
        else:
            self.status = "Failed"
            return False

    def get_transaction_details(self):
        return f"Txn: {self.payment_id} | Order: {self.order.order_id} | Amount: ${self.amount:.2f} | Status: {self.status}"
