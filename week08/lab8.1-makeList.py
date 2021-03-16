# this program make a list/array of random numbers
# Author: Sarah McNelis

import numpy as np 

# set absolute values into variables at the beginning of prog - better practice
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)