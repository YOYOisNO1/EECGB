def program1287():
    n, p = map(int, input().split())
    n -= p
    f = False
    for i in range(100):
        s = bin(n)
        #print(n, s, i + 1)
        if len(s) - 2 >= i + 1 >= s.count('1') > 0 and n > 0:
            k = i + 1
            f = True
            break
        else:
            n -= p
    if f:
        print(k)
    else:
        print(-1)
    
    