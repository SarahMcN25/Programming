# this prog saves the plot as png
# Auhtor: Sarah McNelis

# this porgram adds a legend, title and axis labels to the plot
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

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color= 'r') #show y = x² in color on plot

plt.title("Random Plot") 
plt.xlabel("Salaries")
plt.ylabel("Ages")
plt.legend()
#plt.show()
plt.savefig('prettier-plot.png')