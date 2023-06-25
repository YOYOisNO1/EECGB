def program2541():
    n,m = map(int,input().split())
    l = map(int,input().split())
    l.sort()
    ans = l[n-1]-l[0]
    for i in xrange(1,m-n+1):
    	if l[n+i-1] - l[i] < ans:
    		ans = l[n+i-1] - l[i]
    print(ans)