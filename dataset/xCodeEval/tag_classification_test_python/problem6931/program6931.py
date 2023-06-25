    #!/usr/bin/python
def nextInt(): return int(input().strip())
def next(): return input().strip()
def toInt(input): return int(input)-1
    
def solve(x):
    	cur, ret = x, 0
    	done = [False for i in xrange(n)]
    	
    	while 1:
    		found = False
    		for i in xrange(n):
    			if not done[i] and c[i] == cur:
    				l = 0
    				for j in a[i]:
    					if done[j]:
    						l+=1
    				if l == len(a[i]):
    					ret+=1
    					done[i] = True
    					found = True
    					break
    		if not found:
    			ret+=1
    			cur=(cur+1)%3
    		finish = 0
    		for i in xrange(n):
    			if done[i]:
    				finish+=1
    		if finish == n:
    			break
    	return ret
    
    
    
    n = nextInt()
    a, g = [], []
    c = map(toInt, next().split())
    
    for i in xrange(n):
    	line = map(toInt, next().split())[1:]
    	a.append(line)
    
    ret = 100000000;
    for i in xrange(3):
    	local = solve(i)
    	if (ret > local):
    		ret = local
    
    print(ret)
    
    
    