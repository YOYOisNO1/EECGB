def program13():
    s = input().split()
    p1 = int(s[0])
    t1 = int(s[1])
    s = input().split()
    p2 = int(s[0])
    t2 = int(s[1])
    s = input().split()
    h = int(s[0])
    s = int(s[1])
    dp = [1145141919810] * (h+5)
    dp[0] = 0
    for i in range(1,h+1):
        dp[i] = min(dp[max(0,i-(p1-s))]+t1,dp[max(0,i-(p2-s))]+t2)
        for j in range(1,i+1):
            if(t1 * j >= t2):
                dp[i] = min(dp[i],dp[max(0,i-(j-1)*(p1-s)-((j*t1-t2)//t2)*(p2-s)-(p1+p2-s))]+t1*j)
            if(t2 * j >= t1):
                dp[i] = min(dp[i],dp[max(0,i-(j-1)*(p2-s)-((j*t2-t1)//t1)*(p1-s)-(p1+p2-s))]+t2*j)
    print(dp[h])