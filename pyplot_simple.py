"""
A simple list plot with matplotlib.pyplot
"""

import numpy as np
import matplotlib.pyplot as plt

length = 5
	
fig, ax = plt.subplots()
line, = ax.plot([], [], color='blue',marker='o',linestyle='None')
ax.set_ylim(-1, (length-1)**2+1)
ax.set_xlim(-1, length)
xdata,ydata = [x for x in range(0,length)],[x**2 for x in range(0,length)]
line.set_data(xdata,ydata)
ax.grid()
plt.xlabel("x")
plt.ylabel("x^2")
plt.title("A simple plot")

plt.show()