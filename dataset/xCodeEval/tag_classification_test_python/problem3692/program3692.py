def program3692():
    x = input()
    x = x.split()
    n,k = map(int, x)
    
    y = input()
    y = y.split()
    for i in range(n):
    	y[i] = [int(y[i]), i+1]
    	
    y.sort()
    
    temp = 0
    ans = 0
    while(ans<n and temp + y[ans][0]<=k):
    	temp = temp + y[ans][0]
    	ans += 1
    
    print((ans))
    for i in range(ans):
    	print((y[i][1],) end=' ')