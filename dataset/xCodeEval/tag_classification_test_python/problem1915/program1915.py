def function():
    	n=input()
    	x=input()
    	l=map(int,x.split())
    	no8=x.count('8')
    	maxsets=n/11
    	if maxsets>no8:
    		return no8
    	else:
    		return maxsets
    print(function())