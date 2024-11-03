# 99DaysWithCPC- Machine Learning challenge

# local scope

"""
A variable created inside a function
is available inside that function
"""


def local_scope():
    a = 435
    print(a)


local_scope()

# function inside a function


def firstFunc():
    x = 6887

    def secFunc():
        print(x)

    secFunc()


firstFunc()

# Global scope

"""
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local
"""

aa = 9898


def newFunc():
    print(aa)


newFunc()

# Naming Variable

q = 9999


def newFunc2():
    q = 8989
    print(q)


newFunc2()
print(q)

print("-----Using Global Keyword-----")


def newFunc3():
    global franc
    franc = 5000


newFunc3()
print(franc)


p = 3457


def newFunc4():
    global p  # To change the value of a global variable inside a function
    p = 890


newFunc4()
print(p)

# non local using nonlocal keyword


def myFunc1():
    h = "Jane"

    def myFunc2():
        nonlocal h
        h = "hello"

    myFunc2()
    return h


print(myFunc1())


print("-----Exercise-----")

# exercise
# create 2 global variables called 'multiplier' and has_calculated
# multiplier should have any integer and has_calculated should be set to the boolean False

# then create a function called multiply_calculator that takes one argument and calculates
# the multiplication of that number
# inside of the function multiply the parameter with the global variable multiplier
# once the calculation is done set has_calculated to True
# store that new number a variable called result and return it
# print the return value of the function (after it was called with the number)


multiplier = 5
has_calculated = False


def multiply_calculator(number):
    global has_calculated
    has_calculated = True
    result = number * multiplier
    return result


print(multiply_calculator(10))
print(has_calculated)
