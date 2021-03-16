# this prog increases all the salaries by 5%
# Author: Sarah McNelis

import numpy as np

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

#np.random.seed(1) # this is so that the "random" numbers are the same each time to make it easier to debug.
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
#print (salaries)

salariesMult = salaries * 1.05 # adds 5% by multiplying by 1.05
print(salariesMult)

newSalaries = salariesMult.astype(int) # this converts float array to int array or floors it
print(newSalaries)