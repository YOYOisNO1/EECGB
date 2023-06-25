def program2222():
    grid = []
    grid2 = []
    for i in range(3):
    	s = list(input().split())
    	grid.append(s)
    	s = "".join(s)
    	grid2.append(s)
    
    s = input()
    for i in range(3):
    	s = list(input().split())
    	grid.append(s)
    	s = "".join(s)
    	grid2.append(s)
    
    s = input()
    for i in range(3):
    	s = list(input().split())
    	grid.append(s)
    	s = "".join(s)
    	grid2.append(s)
    
    a,b = map(int,input().split())
    
    if (a)%3==0:
    	x = 3
    elif (a)%3==1:
    	x = 1 
    else:
    	x = 2
    
    if (b)%3==0:
    	y = 3
    elif (b)%3==1:
    	y = 1 
    else:
    	y = 2
    
    flag = 0
    for i in range(3*(x-1),3*(x-1)+3):
    	for j in range(3*(y-1),3*(y-1)+3):
    		if grid2[i][j] =='.':
    			flag = 1
    
    if not flag:
    	for i in range(9):
    		li = list(grid2[i])
    		for j in range(9):
    			if grid2[i][j]=='.':
    				li[j] = '!'
    		grid2[i] = "".join(li)
    	for i in range(9):
    		print(grid2[i][:3]+" "+grid2[i][3:6]+" "+grid2[i][6:])
    		if (i+1)%3==0:
    			print()
    else:
    	for i in range(9):
    		li = list(grid2[i])
    		for j in range(9):
    			if 3*(x-1)<=i<=3*(x-1)+2 and 3*(y-1)<=j<=3*(y-1)+2:
    				if grid2[i][j]=='.' :
    					li[j] = '!'
    		grid2[i] = "".join(li)
    	for i in range(9):
    		print(grid2[i][:3]+" "+grid2[i][3:6]+" "+grid2[i][6:])
    		if (i+1)%3==0:
    			print()