def program3340():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    if(l[0] != 0):
    	print(1)
    	sys.exit()
    for i in range(n):	
    	if(l[i] != 0):
    		print(i)
    		break
    	if(i == n-1):
    		print(n)