def program663():
    import math
    f = math.factorial
    n, k = map(int,input().split(' '))
    diff = n-k
    res = 0
    res = diff**diff
    res = res * (k**(k-1))
    print(res) % (10**9+7)
    