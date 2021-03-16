# this program makes a scatter plot of ages and salaries
# Author: Sarah McNelis

import numpy as np 
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1) #to keep random numbers same each time prog is run
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size= numberOfEntries)

plt.scatter(ages, salaries)
plt.show()