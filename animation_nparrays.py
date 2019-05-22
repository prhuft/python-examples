""" Simple animation example with numpy arrays and fig.canvas.draw() instead 
	of matplotlib.animation.
"""

## LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

xpts = np.array(np.linspace(0,10,100))
ypts = np.sin(xpts)+2

# initialize the figure and axes
fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_ylim(0,10)
ax.set_xlim(0,10)
ax.set_axis_off()
ax.set_aspect(aspect='equal')
ax.set_facecolor('black')

fig.patch.set_facecolor('black')
fig.add_axes(ax)
plt.ion() # set interactive mode on

line, = ax.plot(xpts,ypts,color='red',lw=3)

plt.show()

iters = 10
for i in range(0,iters):
	
	# wait .5 s between iterations
	time.sleep(.5)
	
	ypts = np.sin(xpts+i)+2

	line.set_data(xpts,ypts)
	line, = ax.plot(xpts,ypts)
	
	fig.canvas.draw()
	fig.canvas.flush_events()
	