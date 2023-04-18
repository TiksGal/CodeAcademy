class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"


product = Product("Table", 299.99)
print(product)
print(repr(product))
