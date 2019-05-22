""" Simple animation example with numpy. uses fig.canvas.draw() instead of 
	matplotlib.animation
"""

## LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math as m
from random import random as rand

xpts = np.array(np.linspace(0,10,100))
ypts = np.sin(xpts)+2

# initialize the figure
fig = plt.figure()

# build an axes object that will show the plot in our figure
ax = fig.add_subplot(111)
ax.set_ylim(0,10)
ax.set_xlim(0,10)
ax.set_axis_off()
ax.set_aspect(aspect='equal')
ax.set_facecolor('black')

# add the axes object to the figure, and change the forecolor
fig.add_axes(ax)
fig.patch.set_facecolor('black')

# the initial plot line. note the comma after the variable name
line, = ax.plot(xpts,ypts,color='red',lw=3)

# Set "interactive mode" on (required for animation to work), and show the plot
plt.ion()
plt.show()

# Run 100 frames of the animation
iters = 100
for i in range(0,iters):

	# update the y-position
	ypts = np.sin(xpts+i)+5

	line.set_data(xpts,ypts)

	# update the plot
	fig.canvas.draw()
	fig.canvas.flush_events()
	