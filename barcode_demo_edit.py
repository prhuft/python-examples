"""
============
Barcode Demo
============

This demo shows how to produce a one-dimensional image, or "bar code".
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# the bar
x = np.where(np.random.rand(100) > 0.7, 1.0, 0.0)

axprops = dict(xticks=[], yticks=[])
barprops = dict(aspect='auto', cmap=plt.cm.binary, interpolation='nearest')

fig = plt.figure()

# a vertical barcode
ax1 = fig.add_axes([0.1, 0.3, 0.1, 0.6], **axprops)
bar1 = ax1.imshow(x.reshape((-1, 1)), **barprops)

# a horizontal barcode
ax2 = fig.add_axes([0.3, 0.1, 0.6, 0.1], **axprops)
bar2 = ax2.imshow(x.reshape((1, -1)), **barprops)

## Try to plot w/o imshow
# fig.add_axes(ax1,ax2)
# ax1.plot(x,color='blue',lw=3)

plt.show()

def update(i):
	""" update the bar data """
	bar1.set_data(np.where(np.random.rand(100) > 0.7, 1.0, 0.0))
	bar2.set_data(np.where(np.random.rand(100) > 0.7, 1.0, 0.0))
	# Concatenate the lists, then return as a tuple
	return bar1,bar2

# Run the animation
anim = animation.FuncAnimation(fig, update, interval=10)
plt.show()

#############################################################################
#
# ------------
#
# References
# """"""""""
#
# The use of the following functions, methods and classes is shown
# in this example:

import matplotlib
matplotlib.axes.Axes.imshow
matplotlib.pyplot.imshow
