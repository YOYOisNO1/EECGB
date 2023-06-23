    #!/usr/bin/env python
    import sys
     
    stage = []
     
    for i in range(8):
    stage.append(list(input()))
     
def backtrack(row, col):
    	for dx in (-1, 0, 1):
    		for dy in (-1, 0):
    			if row + dy in range(8) and col + dx in range(8):
    				if row != 0:
    					if stage[row + dy][col + dx] != 'S' and stage[row + dy - 1][col + dx] != 'S':
    						if backtrack(row + dy - 1, col + dx):
    							return 1
    				else:
    					return 1
    	return 0
    
    if backtrack(7, 0):
    	print "WIN"
    else:
    	print "LOSE"