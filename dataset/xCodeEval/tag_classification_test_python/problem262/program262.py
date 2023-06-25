def program262():
    n,c=map(int,input().split())
    L=map(int,input().split())
    M=[]
    for x in xrange(n-1):
    	M.append(L[x] - L[x+1])
    x=M.index(max(M))
    #print(M)
    l=max(M)-c
    if(l<0):
    	print("0")
    else:
    	print(l)