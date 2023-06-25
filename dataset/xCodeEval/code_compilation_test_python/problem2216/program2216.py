def program2216():
    h = map(int,input().split())
    u = map(int,input().split())
    ans = 0
    for i in range(input()):
    	a = map(int,input().split())
    	if (a[0]*h[0] + a[1]*h[1] + a[2]) * (a[0]*u[0] + a[1]*u[1] + a[2]) < 0: ans += 1
    print ans