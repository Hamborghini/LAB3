class MenuItem:
    def __init__(self, item_id, name, description, price, is_available=True):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
        self.is_available = is_available

    def update_availability(self, status: bool):
        self.is_available = status

    def update_price(self, new_price: float):
        if new_price >= 0:
            self.price = new_price

    def get_info(self):
        return f"{self.name} - ${self.price:.2f} ({'Available' if self.is_available else 'Out of Stock'})"


class Menu:
    def __init__(self):
        self._items = {}

    def add_item(self, menu_item: MenuItem):
        self._items[menu_item.item_id] = menu_item

    def remove_item(self, item_id):
        if item_id in self._items:
            del self._items[item_id]

    def get_available_items(self):
        return [item for item in self._items.values() if item.is_available]