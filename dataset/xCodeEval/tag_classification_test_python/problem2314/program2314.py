def program2314():
    n = input()
    
    ans = 0
    l = [100, 20, 10, 5, 1]
    i = 0
    while n > 0:
        ans += (n // l[i])
        n %= l[i]
    
        i += 1
    
    print(ans)