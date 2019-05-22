"""
	Simple timed loop
	Preston Huft
"""

from time import time

for i in range(0,10):
    t = time()
    while True:
        if time()-t > 1:
            break
    print(time())