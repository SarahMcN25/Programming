# this program plots the function y = x²
# Author: Sarah McNelis

import matplotlib.pyplot as plt 
import numpy as np 

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply by itself to give x²

plt.plot(xpoints, ypoints)
plt.show() 