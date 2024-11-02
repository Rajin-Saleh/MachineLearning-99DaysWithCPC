#   Short hand if else

a = int(input("Enter a number: "))
b = int(input("Enter a new number: "))

print(f"This is bigger {a}") if a > b else print(f"This one is bigger {b}")


# # And + or

if True and True and False or True:
    print("True")


# Exercise

money = 100
hungry = False
bored = False

# check if money > 80 and if hungry is true or if bored

if money > 80 and hungry is True or bored is True:
    print("Eat something Fancy")
else:
    print("Eat something cheap! or don't eat anything.")

# Nesting a if Statement
x = "b"

if x in ["a", "b", "1"]:
    print("a is in the list")
    if x.isalpha():
        print("It is a letter")

        if True:
            print("Something")


# Exercise

money2 = 100
hungry2 = True
bored2 = True

# create a nested if statement that runs of all 3 conditions are true
# (money > 80 for the first one)

if money2 > 80:
    print("I have enough money.")
    if hungry2 is True:
        print("and I am hungry")
        if bored2 is False:
            print("Eat something Fancy")
