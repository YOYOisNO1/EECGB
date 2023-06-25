def program639():
    ii=lambda:int(input())
    kk=lambda:map(int,input().split())
    ll=lambda:list(kk())
    n,k=kk()
    if n < 7:
    	print(k)
    	exit()
    d = [set() for i in range(7)]
    for _ in range(k):
    	a,b=kk()
    	a,b=a-1,b-1
    	d[a].add(b)
    	d[b].add(a)
    maxi=0
    for a in range(7):
    	for b in range(a+1,7):
    		maxi=max(maxi, k-len(d[a]&d[b]))
    print(maxi)