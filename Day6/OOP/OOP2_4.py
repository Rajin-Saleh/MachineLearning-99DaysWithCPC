# 99DaysWithCPC - Machine Learning

# Class vs Static Methods


# How to create a class:

import csv


class Item:
    pay_rate = 0.8  # after 20% discount
    all = []

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

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("Day6/OOP/Items.csv", "r") as f:  # Provide the actual path here
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get("name"),
                    price=float(item.get("price")),
                    quantity=int(item.get("quantity")),
                )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.3: 5.0, 10:0
        if isinstance(num, float):
            # count out the float that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


print(Item.is_integer(7.0))
