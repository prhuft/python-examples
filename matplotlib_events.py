"""
	Matplotlib event handling. Code taken from or adapted from examples here:
	https://matplotlib.org/users/event_handling.html
	
	Preston Huft, April 2019
	To run one of the examples, make sure all others are commented out. 
"""

import matplotlib.pyplot as plt
import numpy as np
import time

###############################################################################
## EX. 1: PRINT MOUSE CLICK EVENT DATA WHEN CLICK AREA IS WITHIN THE FIGURE
###############################################################################

# Generic plot
# fig, ax = plt.subplots()
# ax.plot(np.random.rand(10))

# def onclick(event):
	# """Show click data if click occurs in the region of the plot in the 
		# figure."""
	# print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
		  # ('double' if event.dblclick else 'single', event.button,
		   # event.x, event.y, event.xdata, event.ydata))

# cid = fig.canvas.mpl_connect('button_press_event', onclick)
# plt.show()

# fig.canvas.mpl_disconnect(cid)

###############################################################################
## EX. 2: PRINT KEYPRESS EVENT DATA
###############################################################################

# Generic plot to be used with all examples
fig, ax = plt.subplots()
ax.plot(np.random.rand(10))

def onkeypress(event):
	"""Show key press data while plot is shown."""
	print('key pressed: ', event.key)
	
cid = fig.canvas.mpl_connect('key_press_event',onkeypress)
plt.show()

fig.canvas.mpl_disconnect(cid)

###############################################################################
## EX. 3: CHANGE GLOBAL VARIABLE ON KEYPRESS
###############################################################################

# def onkeypress(event):
	# """Show key press data while plot is shown. """
	# key = event.key
	# print('key pressed: ', key)
	
	# global phi # access the global var
	# phi+=1
	
	# if key == "ctrl+c":
		# fig.canvas.mpl_disconnect(cid) # disconnect the listener

# fig, ax = plt.subplots()
# xpts = np.linspace(0,10,num=100)
# phi = 0
# line, = ax.plot(xpts,np.sin(xpts))

# turn on the event listener. this MUST be placed after the figure has been
# instantiated, and before the plot is shown.  
# cid = fig.canvas.mpl_connect('key_press_event',onkeypress)

# plt.ion()
# plt.show()

# while True:
	# try:
		# time.sleep(.1)
		# line.set_data(xpts,np.sin(xpts+phi))
		# fig.canvas.draw()
		# fig.canvas.flush_events()
	# except KeyboardInterrupt:
		# raise
