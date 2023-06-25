def program557():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 1
    cur = m
    for i in range(n):
    	if a[i] > cur:
    		ans+=1
    		cur = m-a[i]
    	else:
    		cur -= a[i]
    print(ans)