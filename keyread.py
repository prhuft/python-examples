""" Simple example of reading keypresses in Windows.
	Preston Huft, April 2019
	
	This is not the way to "listen" asynchronously for key presses. The 
	function getch() used below simply waits for a keypress once called, and
	all other code that follows does not execute until a keypress is received.
	See matplotlib.events.py for key press event handling. 
"""

from msvcrt import getch

## example of waiting continuously for presses. maybe useful in a chess game? 
# while True:
	# key = ord(getch())
	# if key == 27: # ESC
		# break
	# elif key == 224:
		# key = ord(getch())
		# if key == 72:
			# print("up")
		# elif key == 80:
			# print("down")
		# elif key == 75:
			# print("left")
		# elif key == 77:
			# print("right")
	#print(key)

## attempt to run a loop, check each iteration if a key was pressed. supposed
## to be similar to asynchronous key presses...
while True: 
	if (getch()):
		print(ord(getch()))
	else:
		print("no key pressed")
	if key == 27: # ESC
		break
	
