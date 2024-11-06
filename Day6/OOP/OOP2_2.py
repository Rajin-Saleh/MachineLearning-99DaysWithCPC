## 99DaysWithCPC

# Constructor

# How to create a class:
class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert (
            quantity >= 0
        ), f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


# How to create an instance of a class
item1 = Item("Phone", 100, 1)


# How to create an instance of a class (We could create as much as instances we'd like to)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
