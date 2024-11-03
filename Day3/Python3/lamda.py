# 99DaysWithCPC - Machine Learning

# Lambda Function in Python

# single line : functions
# lambda para:expression
"""
lambda x:x+1
"""

a = lambda x: x + 1
simple_calc = lambda a, b: a + b

print(a(10))
print(simple_calc(2, 3))

# some functions want other functions as argument
# sort([1,5,2,3,4], func)

# graphical user interface

# exercise

print("-----Exercise-----")

# exercise
# create a lambda function that accepts 1 integer argument
# if the integer is > 5 return hello
# otherwise return bye

x = lambda x: "hello" if x > 5 else "bye"
print(x(10))
