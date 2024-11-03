# 99DaysWithCPC - Machine Learning

# More advanced way to loop over data

# Manipulating lists & for loops

# often to merge lists and loop over the result

# warehouse inventory ( item names and numbers )
inventory_names = [
    "Screws",
    "Wheels",
    "Metal parts",
    "Rubber bits",
    "Screwdrivers",
    "Wood",
]
inventory_numbers = [43, 12, 95, 421, 23, 43]

# print(list(zip(inventory_names, inventory_numbers)))
# Hardly going to use in coding this way

for name, number in zip(inventory_names, inventory_numbers):  # Good way
    print(f"{name} current index: {number}")

print("-----Enumerate function way-----")

# enumerate function - get current index

# print(list(enumerate(inventory_names))) # unusual way
for index, name in enumerate(inventory_names):
    print(f"{index} : {name}")
    if index == len(inventory_names) // 2:
        print("Half way done!")

# exercise

print("-----Exercise-----")

# Exercise
# combine zip and enumerate to get 'Screws [id: 0] - inventory: 43'

for thing in zip(inventory_names, inventory_numbers):
    print(f"{thing} ")  # made a tuple

print("-----Again------")

for index, inventory_tuple in enumerate(zip(inventory_names, inventory_numbers)):
    print(f"{inventory_tuple[0]} [id : {index}] - inventory: {inventory_tuple[1]}")
