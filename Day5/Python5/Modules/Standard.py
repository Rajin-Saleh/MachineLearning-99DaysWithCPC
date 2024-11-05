# 99DaysWithCPC - Machine Learning

# Modules - extra part we can attach in program

# 1. we can import from python library
# 2. Import additional modules made by other
# (need to install in pc)

import random, string
from math import floor as sudo
from datetime import datetime as dt

random_number = random.randint(0, 10)
print(random_number)
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(test_list))
print(string.ascii_uppercase)


print(sudo(4.9))
print(dt.now())


# time generator

import time


def time_generator(interval, duration):
    start = time.time()
    end = start + duration

    while time.time() < end:
        current = time.strftime("%Y - %m - %d %H:%M:%S", time.localtime())
        yield current
        time.sleep(interval)


for current in time_generator(1, 5):
    print(current)
