def program964():
    from __future__ import division
    from math import ceil
    from collections import Counter
    
    x, y = input("").split(" ")
    x, y = int(x), int(y)
    y = [y, y, y]
    count = 0
    while not (y[0] == y[1] == y[2] == x):
    	y.sort()
    	y[0] = min(y[1] + y[2] - 1, x)
    	count += 1
    print(count)