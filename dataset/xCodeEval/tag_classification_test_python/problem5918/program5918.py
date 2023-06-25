def program5918():
    from math import gcd
    n = int(input())
    arr = map(int, input().split())
    arr = list(map(lambda x: x-1, arr))
    
    res = 1
    for i in range(n):
        p, k = 0, i
        for j in range(n):
            k = arr[k]
            if k == i:
                p = j
                break
        if k != i:
            print(-1)
            exit()
        p += 1
        if p % 2 == 0: p //= 2
        res = res * p // gcd(res, p) 
    print(res)