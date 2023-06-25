def program7357():
    #yeh dil maange more
    n,m = map(int,input().split())
    if n<m:n,m = m,n
    ans = 0
    d = {0:0,1:1,2:2,3:3,4:2,5:1}
    if m==1:ans=d[n%6]
    elif m==2:
    	if n==3:ans=2
    	elif n==2:ans=4
    	elif n==7:ans=2
    else:ans =(n*m)%2
    print(n*m-ans)