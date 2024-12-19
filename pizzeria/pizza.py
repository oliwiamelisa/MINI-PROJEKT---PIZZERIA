

class Pizza:
    def __init__(self, pizza_type: str, ingridients: list[str], price: float, size: str):
        self.pizza_type = pizza_type
        self.ingridients = ingridients
        self.price = price
        self.size = size

    def pizza_type(self):
        return f"{self.size.capitalize()} {self.pizza_type}, {self.ingridients} w cenie: {self.price} PLN"
    