def program6616():
    #Bhargey Mehta (Sophomore)
    #DA-IICT, Gandhinagar
    import sys, math, queue, bisect
    #sys.stdin = open("input.txt", "r")
    MOD = 10**9+7
    sys.setrecursionlimit(1000000)
    
    n, k, m = map(int, input().split())
    a = sorted(map(int, input().split()))
    s = sum(a)
    ans = 0
    for i in range(n+1):
        t = m-s*i
        p = (k+1)*i
        if t < 0: break
        rest = n-i
        for ai in a:
            q = min(rest, t//ai)
            t -= q*ai
            p += q
        ans = max(ans, p)
    print(ans)