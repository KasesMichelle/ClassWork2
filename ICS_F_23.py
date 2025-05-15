class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item_name: str, qty: int, unit_price: float):
        self.items.append((item_name, qty, unit_price))

    def remove_item(self, item_name: str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self) -> float:
        total = 0.0
        for name, qty, price in self.items:
            total += qty * price
        return total

    def cart_contents(self):
        print("Cart Contents: ")
        for name, qty, price in self.items:
            print(f"  {name}:- {qty} @ Ksh {price:.2f} each")
        print(f"Total: K
