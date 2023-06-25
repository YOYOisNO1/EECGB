def program2357():
    n = int(input())
    
    ans = 0
    
    while(n != 0):
        if n % 2 == 0:
            ans += n // 2
            break
        ans += 1
    
        p = 3
        tmp = int(n ** 0.5)
        while(p < n):
            if n % p == 0:
                break
    
            if p > tmp:
                p = n
            else:
                p += 2
        n -= p
    
    print(ans)