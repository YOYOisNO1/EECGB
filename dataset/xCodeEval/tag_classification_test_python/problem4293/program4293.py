    s=[input() for i in range(8)]
    d=[[16]*8 for i in range(8)]
    deep=0;
    	
def res(a):
    	print(["LOSE","WIN"][a])
    	exit()
    	
def dfs(r,c):
    	global deep,d
    	d[r][c]=deep;
    	deep+=1
    	
    	if r==0 and c==7:
    		maria=True
    		res(True)
    	
    	C=False
    	for i1 in [-1,1,0]:
    		for i2 in [1 ,-1, 0]:
    			if r+i1>=0 and r+i1<=7 and c+i2>=0 and c+i2<=7 and d[r+i1][c+i2]>d[r][c]:
    				C=True
    	
    	if C:
    		for i1 in [-1,1,0]:
    			for i2 in [1 ,-1, 0]:
    				if r+i1>=0 and r+i1<=7 and c+i2>=0 and c+i2<=7 and (d[r+i1][c+i2]>=deep or (i1==0 and i2==0)):
    					A=True	
    					for i in range(8):
    						if s[i][c+i2]=='S' and (min(i+deep,7)==r+i1 or min(i+deep-1,7)==r+i1):
    							A=False
    							break
    					
    					if A:
    						dfs(r+i1,c+i2)		
    						deep-=1
    
    dfs(7,0)
    res(False)