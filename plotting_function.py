# creating the graphing functions
#https://pythonprogramming.net/python-matplotlib-live-updating-graphs/
# https://www.youtube.com/watch?v=Ercd-Ip5PfQ&ab_channel=CoreySchafer
# need a while loop interupt to stop if emergency stop hit
# selection statements to make sure data types are the correct type

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

x_vals = [0, 1, 2, 3, 4, 5]
y_vals = [0, 1, 3, 2, 3, 5]

plt.plot(x_vals, y_vals)


# index = count()

def animate(i):
     x_vals.append(next(index))
     y_vals.append(random.randint(0, 5))


plt.tight_layout()
plt.show()