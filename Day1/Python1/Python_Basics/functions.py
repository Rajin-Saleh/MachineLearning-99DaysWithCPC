# 99DaysWithCPC - Machine Learning


def greet():
    name = input("What is you name? ").title()
    print(f"Your name is {name}")

    age = int(input("What is your age? "))
    print(f"You are {age} years old")


def max_number():
    print("-----Maximum number in 3 number-----")
    n1 = int(input("Enter a random number... "))
    n2 = int(input("Enter a random number... "))
    n3 = int(input("Enter a random number... "))
    biggest_number = max(n1, n2, n3)
    print(f"Maximum Number is {biggest_number}")


def min_number():
    print("-----Minimum number in 3 number-----")
    q1 = int(input("Enter a random number... "))
    q2 = int(input("Enter a random number... "))
    q3 = int(input("Enter a random number... "))
    smallest_number = max(q1, q2, q3)
    print(f"Maximum Number is {smallest_number}")


greet()
max_number()
min_number()
