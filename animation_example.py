"""
This example showcases a sinusoidal decay animation using lists. Not a very 
efficient way to tackle animation. 
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def data_gen(t=0):
	cnt = 0
	while cnt < 1000:
		cnt += 1
		t += 0.1
		# yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
		sin_data = t,np.sin(2*np.pi*t) * np.exp(-t/10.)
		cos_data = t,np.cos(2*np.pi*t) * np.exp(-t/10.)
		yield cos_data,sin_data
		
		# data = np.cos(2*np.pi*t) * np.exp(-t/10.),np.sin(2*np.pi*t) * np.exp(-t/10.)
		# yield data

def init():
	ax.set_ylim(-1.1, 1.1)
	ax.set_xlim(0, 10)
	# ax.set_ylim(-1.1,1.1)
	# ax.set_xlim(-1.1,1.1)
	# del xdata[:]
	# del ydata[:]
	# line.set_data(xdata, ydata)
	# xdata,ydata = [],[]
	line.set_data([],[])
	return line

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


def run(data):
	# update the data
	t, y1 = data[0]
	t, y2 = data[1]
	xdata.append([t,t])
	ydata.append([y1,y2])
	# x,y = data
	# xdata.append(x)
	# ydata.append(y)
	
	#xmin, xmax = ax.get_xlim()
	
	# if t >= xmax:
		# ax.set_xlim(xmin, 2*xmax)
		# ax.figure.canvas.draw()
	#line.set_data(xdata, ydata)
	#line.set_data([t],[y])
	line.set_data(xdata,ydata)

	return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)
plt.show()