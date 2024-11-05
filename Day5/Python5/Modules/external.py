# 99DaysWithCPC - Machine Learning

# External modules

# these are the modules which are not built in and have to install it
# by saying pip3 install pyautogui - for linux


import pyautogui
from time import sleep
import matplotlib.pyplot as plt

# sleep(1)
# pyautogui.write('This is written by a computer', interval = 0.25)

# exercise
# create a graph from any of the examples below
# https://matplotlib.org/3.5.0/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

plt.plot([1, 2, 3, 4, 10, 0, 100, 21, 34, 55, 46, 78, 55])
plt.ylabel("some numbers for the y-axis")
plt.xlabel("some numbers for the x-axis")
plt.show()
