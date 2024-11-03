# 99DaysWithCPC- Machine Learning challenge

# Scope in Python

# import math

# w = abs(-7.86)
# x = math.ceil(1.4)
# y = math.floor(1.4)
# z = math.pi

# print(w)
# print(x)
# print(y)
# print(z)

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
