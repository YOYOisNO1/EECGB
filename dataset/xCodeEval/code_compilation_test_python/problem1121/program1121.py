def program1121():
    import sys
    n,k=[int(x) for x in sys.stdin.readline().split()]
    factors=set()
    for i in range(1,int(n**0.5)+1):
    	if n%i==0:
    		factors.add(i)
    		if i//n!=i:
    			factors.add(n//i)
    
    if k>len(factors):
    	print("-1")
    else:
    	print(sorted(factors)[k-1]))
    