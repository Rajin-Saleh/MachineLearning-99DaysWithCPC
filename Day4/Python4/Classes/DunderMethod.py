# 99DaysWithCPC - Machine Learning

# OOP - Object Oriented Programming

# __Dunder__methods

"""
A dunder method is a method that is not called by the user
instead, it is called by python when something happens
__init__ is called when the object is created
__len__ is created when the object is passed into len()
__abs__ is called when the object is passed into abd()
"""

# from earlier


class Monster:
    # dunder method

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy

    def __call__(self):
        print("The monster was called")

    def __add__(self, other):
        return self.health + other

    def __str__(self):  # exercise
        return f"A monster with health {self.health} and energy {self.energy}"

    # methods

    def attack(self, ammount):
        print("The monster has attacked!")
        print(f"{ammount} of damage was dealt")
        self.energy -= 20  # noqa: F821
        print(self.energy)  # noqa: F821

    def move(self, speed):
        print(f"The monster has moved in {speed}km/h speed.")


monster1 = Monster(19, 20)
print(monster1.__dict__)
print(vars(monster1))

print(monster1 + 10)


# exercise

"""
research __str__ method and figure out he way to use it
"""
print("------Exercise------")

print(str(monster1))
print(monster1)


# this was challenging to learn by fun
