class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self, item_name: str, qty: int, unit_price: float):
        self.items.append((item_name, qty, unit_price))

    def remove_items(self, item_name: str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self) -> float:
        total = 0
        for name, qty, price in self.items:
            total += qty * price
        return total

    def summary(self):
        print("Cart Contents")
        for name, qty, price in self.items:
            print(f"{name}: {qty} @ Ksh {price:.3f} each")
        print(f"Total: Ksh {self.calculate_total():.2f}\n")


def checkout(cart: ShoppingCart):
    cart.summary()


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_items("Kiwi", 50, 76)
    cart.add_items("Mango", 87, 54)
    cart.add_items("Oranges", 44, 65)

    print(">>> Regular Cart <<<")
    checkout(cart)
