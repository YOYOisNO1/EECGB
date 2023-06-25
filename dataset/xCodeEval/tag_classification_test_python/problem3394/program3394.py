def program3394():
    #!/usr/bin/python
    import sys
    from sys import stdin
    import math
    
    count = 0
    lines = []
    
    for i in range(0,8):
    	lines.append(stdin.readline())
    
    for i in range(0, 8):
    	row = 0
    	for j in range(0, 8):
    		if lines[i][j] == "B":
    			row += 1
    	if row == 8:
    		count += 1
    
    for i in range(0, 8):
    	col = 0
    	for j in range(0, 8):
    		if lines[j][i] == "B":
    			col += 1
    	if col == 8:
    		count += 1
    
    if count == 16:
    	print(8)
    else:
    	print(count)
    