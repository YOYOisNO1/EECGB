def program2220():
    #Abhigyan Khaund - syl
    # n = int(input())
    # v1,v2,v3,vm = map(int, input().split())
    c = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(3):
    	k = input().split()
    	c[1].append(list(k[0]))
    	c[2].append(list(k[1]))
    	c[3].append(list(k[2]))
    input()
    
    for i in range(3):
    	k = input().split()
    	c[4].append(list(k[0]))
    	c[5].append(list(k[1]))
    	c[6].append(list(k[2]))
    
    input()
    
    for i in range(3):
    	k = input().split()
    	c[7].append(list(k[0]))
    	c[8].append(list(k[1]))
    	c[9].append(list(k[2]))
    
    x,y = map(int, input().split())
    
    dx = x%3
    dy = y%3
    if(dx==0):
    	dx = 3
    if(dy==0):
    	dy = 3
    go = 1
    if(dx==1 and dy==1):
    	go = 1
    elif(dx==1 and dy==2):
    	go = 2
    elif(dx==1 and dy==3):
    	go = 3
    elif(dx==2 and dy==1):
    	go = 4
    elif(dx==2 and dy==2):
    	go = 5
    elif(dx==2 and dy==3):
    	go = 6
    elif(dx==3 and dy==1):
    	go = 7
    elif(dx==3 and dy==2):
    	go = 8
    elif(dx==3 and dy==3):
    	go = 9
    
    count = 0
    
    for i in range(3):
    	for j in range(3):
    		if(c[go][i][j]=='.'):
    			c[go][i][j] = '!'
    			count+=1
    if(count==0):
    	for go in range(1,10):
    		for i in range(3):
    			for j in range(3):
    				if(c[go][i][j]=='.'):
    					c[go][i][j] = '!'
    					# count+=1
    
    
    for i in range(1,4):
    	print('').join(c[i][0])+ ' ',
    print(for) i in range(1,4):
    	print('').join(c[i][1])+ ' ',
    print(for) i in range(1,4):
    	print('').join(c[i][2])+ ' ',
    print(print)
    for i in range(4,7):
    	print('').join(c[i][0])+ ' ',
    print(for) i in range(4,7):
    	print('').join(c[i][1])+ ' ',
    print(for) i in range(4,7):
    	print('').join(c[i][2])+ ' ',
    print(print)
    for i in range(7,10):
    	print('').join(c[i][0])+ ' ',
    print(for) i in range(7,10):
    	print('').join(c[i][1])+ ' ',
    print(for) i in range(7,10):
    	print('').join(c[i][2])+ ' ',
    print(print)