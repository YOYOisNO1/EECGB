def program4647():
    n,k=map(int,input().split())
    e=input()
    a=[[-1,-1] for i in xrange(26)]
    for i in xrange(n):
    	if a[ord(e[i])-ord('A')][0]==-1:
    		a[ord(e[i])-ord('A')][0]=i
    		a[ord(e[i])-ord('A')][1]=i
    	else:
    		a[ord(e[i])-ord('A')][1]=i
    #print(a)
    z=[0]*n
    z1=[0]*n
    #print(z)
    for i in xrange(26):
    
    	if a[i][0]!=-1:
    		#print(a[i][0],a[i][1])
    		z[a[i][0]]=1
    		z1[a[i][1]]=-1
    #print(z)
    zz=0
    pos=1
    for i in xrange(n):
    	zz+=z[i]
    	if zz>k:
    		pos=0
    	zz+=z1[i]
    if pos==0:
    	print('YES')
    else:
    	print('NO')