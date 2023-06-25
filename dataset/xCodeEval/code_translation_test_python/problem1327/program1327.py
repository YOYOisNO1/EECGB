def program1327():
    v1,v2 = map(int,input().split())
    t,d = map(int,input().split())
    dp = [0] * t
    dp[0] = v1
    dp[-1] = v2
    for i in xrange(t-2,0,-1):
    	dp[i] = min(dp[-1] + (t-1)*d-(i*d),dp[0] + i*d) 
    print(sum(dp))