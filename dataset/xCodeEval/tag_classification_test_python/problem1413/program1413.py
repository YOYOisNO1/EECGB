def solve(a,b):
    	if b==1:
    		return a
    	k=int(a/b)
    	c=b-a%b
    	if c==1:
    		return k+a%b +1
    	else:
    		return k+solve(c,a%b) +1
    
    (a,b) = map(int, input().split(' '))
    
    print(solve(a,b))