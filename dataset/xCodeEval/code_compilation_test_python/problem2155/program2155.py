def program2155():
    #input
    n,m=map(int,input().split())
    xlist=[int(x) for x in input().split()]
    
    #variables
    plist=xlist[:]
    
    #main
    xlist.sort()
    
    for i in range(n):
    	if xlist[plist[i]]%2==0:
    		xlist[i]='0'
    	else:
    		xlist[i]='1'
    
    print(''.join([xlist[i]+' ' for i in range(n)]))