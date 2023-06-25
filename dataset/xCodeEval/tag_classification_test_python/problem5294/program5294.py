def program5294():
    
    import math
    
    n, m = map(int, input().split())
    
    dp = [0, 1]
    s = [0, 1]
    
    for i in range(2,n+1):
        y = i**0.5
        k = math.ceil(y)
    
        res = s[-1]
        #print("res",res)
    
        l = i // (1 + 1) + 1
        r = i // 1
        # print("l, r",l,r)
        res += (r - l + 1) * dp[1]
    
        for j in range(2,k+int(k*k==i)):
            l = i//(j+1)+1
            r = i//j
            #print("l, r",l,r)
            res += (r-l+1)*dp[j]
            if i//j > y:
                res += dp[r]
    
    
        s.append((s[-1]+res)%m)
        dp.append(res%m)
    
    
    print(dp[n])