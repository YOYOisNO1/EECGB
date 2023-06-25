def program772():
    import sys
    n,k=[int(x) for x in sys.stdin.readline().split()]
    counter=1
    tobeprinted=[]
    while counter!=k:
    	for i in range(2,int(n)+1):
    		if n%i==0:
    			tobeprinted.append(i)
    			n=n//i
    			counter+=1
    			break
    	if n==1:
    		print("-1")
    		exit()
    tobeprinted.append(n)
    print(*tobeprinted)