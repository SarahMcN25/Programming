# this program plots a histogram of the salaries from lab8.1
# Author: Sarah McNelis

import numpy as np 
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1) #to keep random numbers same each time prog is run
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

plt.hist(salaries) # to get histogram
plt.show() # to show histogram

