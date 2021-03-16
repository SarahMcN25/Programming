# this program adds 5000 to salaries 
# Author: Sarah McNelis

import numpy as np 

# set absolute values into variables at the beginning of prog - better practice
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)

salariesPlus = salaries + 5000 # can only add this way if using numpy
print (salariesPlus)