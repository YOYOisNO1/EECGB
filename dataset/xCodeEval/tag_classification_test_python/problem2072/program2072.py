def program2072():
    n, k, d = map(int, input().split())
    mod = 1000000007
    
    dp_less_than_d = [0 for i in range(101)]
    dp_inc_d = [0 for i in range(101)]
    dp_less_than_d[0] = 1
    
    for i in range(1,n+1):
        for j in range(1,min(k,n)+1):
            if i-j < 0:
                break
    
            if j < d:
                dp_less_than_d[i] = (dp_less_than_d[i]%mod + dp_less_than_d[i-j]%mod) % mod
                dp_inc_d[i] = (dp_inc_d[i]%mod + dp_inc_d[i-j]%mod) % mod
    
            if j >= d:
                dp_inc_d[i] = (dp_inc_d[i]%mod + dp_less_than_d[i-j]%mod) % mod
                dp_inc_d[i] = (dp_inc_d[i]%mod + dp_inc_d[i-j]%mod) % mod
    
    print(dp_inc_d[n])