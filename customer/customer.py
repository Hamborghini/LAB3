class Customer:
    def __init__(self, customer_id, name, email, phone, address):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._phone = phone
        self._address = address
        self._order_history = []

    def get_customer_id(self):
        return self._customer_id

    def get_details(self):
        return {
            "name": self._name,
            "email": self._email,
            "phone": self._phone,
            "address": self._address
        }

    def update_address(self, new_address):
        self._address = new_address

    def update_phone(self, new_phone):
        self._phone = new_phone

    def add_to_history(self, order):
        self._order_history.append(order)
        
    def get_order_history(self):
        return self._order_history