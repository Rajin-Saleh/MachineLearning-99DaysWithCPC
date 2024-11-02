basic_list = [1, 2, 3]
basic_tuple = (1, 2, 3)
basic_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
}
basic_set = {1, 2, 3}
basic_string = "one two three"
basic_num = 3


for x in basic_list:
    print(x)
for x in basic_tuple:
    print(x)
for x in basic_dict.items():
    print(x)
for x in basic_set:
    print(x)
for x in basic_string.capitalize():
    print(x)
for x in range(basic_num):
    print(x)

print("\n\n")

# Exercise

practice_list = [[10, 40, 20, 50], [2, 42, 10], [101, 12, 4]]

"""
use for loop to only print the number below 50
skip values below 10
ends the entire loop if a value is above 100
"""

for nested_list in practice_list:
    print(nested_list)
    for value in nested_list:
        if value > 100:
            break
        if value < 50 and value != 10:
            print(value)
