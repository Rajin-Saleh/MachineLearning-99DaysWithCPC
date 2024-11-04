# 99DaysWithCPC - Machine Learning

# OOP - Object Oriented Programming

# CamelCase naming convention


class Monster:
    health = 90
    energy = 40

    # methods

    def attack(self, ammount):
        print("The monster has attacked!")
        print(f"{ammount} of damage was dealt")
        monster.energy -= 20
        print(monster.energy)

    def move(self, speed):
        print(f"The monster has moved in {speed}km/h speed.")


monster = Monster()
monster1 = Monster()
monster2 = Monster()
monster3 = Monster()

# variable = class() .... this is variable is snake_case and class CamelCase
# print(monster.health)
# print(monster.energy)


# print(health) # going to show error for not mentioning class
