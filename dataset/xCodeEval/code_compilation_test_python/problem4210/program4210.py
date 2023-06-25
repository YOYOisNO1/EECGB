def program4210():
    from math import log2, ceil
    N = int(input())
    if N % 2 == 0:
        N //= 2
        ans = 2 ** ceil(log2(N)) - N
    else:
        ans = (N+1) // 2 - 1
    print(ans)