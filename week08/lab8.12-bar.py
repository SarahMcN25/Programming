# this program makes a bar chart from a list of counties
# Author: Sarah McNelis

import numpy as np 
import matplotlib.pyplot as plt 

possibleCounties = [ 'Clare', 'Kerry', 'Cork', 'Donegal', ' Westmeath']
# array of occurences

counties = np.random.choice(possibleCounties, p=[0.1, 0.3, 0.2, 0.12, 0.28], size=(100))
# pick 100 randomly from possible counties witht he frequence set in p

# now need number of occurences of each county
# this returns a tuple of the unique values and how may time sthey appear
unique, counts = np.unique(counties, return_counts=True)

plt.bar(unique, counts)
plt.show()