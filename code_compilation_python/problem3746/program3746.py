    bb1=[5,4,6]
    bb2=[1,2,4]
    print bb1 ^^ bb2
    exit()
    s=[input() for i in range(8)]
    d=[[16]*8 for i in range(8)]
    deep=0;
    	
def res(a):
    	print ["LOSE","WIN"][a]
    	exit()
    	
def can(r,c,r1,c1):
    	global d
    	return r+r1>=0 and r+r1<=7 and c+c1>=0 and c+c1<=7 and (d[r+r1][c+c1]>d[r][c])
    	
def dfs(r,c):
    	global deep,d
    	d[r][c]=deep;
    	deep+=1
    	
    	if r==0 and c==7:
    		res(1)
    	
    	sw=0
    	for r1 in [-1,1,0]:
    		for c1 in [1 ,-1, 0]:
    			if can(r,c,r1,c1):
    				sw=1
    		
    	if sw:
    		for r1 in [-1,1,0]:
    			for c1 in [1 ,-1, 0]:
    				if can(r,c,r1,c1) or (r1==0 and c1==0):
    					A=True	
    					for i in range(8):
    						if s[i][c+c1]=='S' and (min(i+deep,7)==r+r1 or min(i+deep-1,7)==r+r1):
    							A=False
    					
    					if A:
    						dfs(r+r1,c+c1)		
    						deep-=1
    
    dfs(7,0)
    res(0)