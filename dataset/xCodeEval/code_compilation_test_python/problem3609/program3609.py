def program3609():
    from sys import stdin
    from math import sqrt
    # input = input
    # xrange = range
    input = lambda: stdin.readline().rstrip()
    input = lambda: int(input())
    I=lambda: map(int, input().split())
    n,m = I()
    dp = [0]*(n+1)
    dp[1] = 1
    s = 1
    for x in xrange(2, n+1):
    	w = 0
    	q = int(sqrt(x))
    	q1 = q+(0 if q**2==x else 1)
    	q2 = q1-1
    	for j in xrange(2, q1): #j<sqrt(x)
    		w = (w+dp[x//j])%m
    	for c in xrange(1, q+1):
    		a1 = x//(c+1)
    		a2 = x//c
    		w = (w+(dp[c]*(a2-a1)%m)%m
    	dp[x] = (s + w)%m
    	s = (s+dp[x])%m
    print(dp[n])