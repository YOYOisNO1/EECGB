def program1326():
    n,k,m,d = map(int,input().split())
    ans = m
    for i in range(d):
    	temp = min(m,n//(k*i+1))
    	ans=max(ans,(i+1)*temp)
    print(ans)