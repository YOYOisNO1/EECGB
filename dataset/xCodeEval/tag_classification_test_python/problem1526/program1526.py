def program1526():
    n,m,k=input().split()
    n=int(n)
    m=int(m)
    k=int(k)
    l = list(map(int,input().split()))
    l.sort()
    l.reverse()
    z=k
    f=0
    while(z<m and f<n):
    	z+=l[f]-1
    	f+=1
    if(z>=m):
    	print(f)
    else:
    	print(-1)