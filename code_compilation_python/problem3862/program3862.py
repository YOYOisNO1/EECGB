def program3862():
    s=[]
    for i in range(6):
    	s.append(input())
    a=[[3,3,0,0,4,4,0,0,3,3], [3,3,0,0,4,4,0,0,3,3], [2,2,0,0,3,3,0,0,2,2], [2,2,0,0,3,3,0,0,2,2], [1,1,0,0,2,2,0,0,1,1], [1,1,0,0,2,2,0,0,1,1]]
    mx = -1
    for i in range(6):
    	for j in range(len(s[i])):
    		if s[i][j] == '.' and a[i][j] > mx:
    			mx = a[i][j]
    			ind = [i,j]
    for i in range(6):
    	if i == ind[0]:
    		ss=''
    		for j in range(8):
    			if j == ind[1]:
    				ss+='P'
    			else: ss+=s[i][j]
    		print ss
    	else: print s[i]