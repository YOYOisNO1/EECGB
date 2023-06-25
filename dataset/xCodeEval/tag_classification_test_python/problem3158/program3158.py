    import sys
def fastio():
        from io import StringIO
        from atexit import register
        global input
        sys.stdin = StringIO(sys.stdin.read())
        input = lambda : sys.stdin.readline().rstrip('\r\n')
        sys.stdout = StringIO()
        register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))
    fastio()
    
def debug(*var, sep = ' ', end = '\n'):
        print(*var, file=sys.stderr, end = end, sep = sep)
    
    INF = 10**20
    MOD = 10**9 + 7
    I = lambda:list(map(int,input().split()))
    from math import gcd
    from math import ceil, log2
    from collections import defaultdict as dd, Counter
    from bisect import bisect_left as bl, bisect_right as br
    
    n, a, b = I()
    area = 6 * n
    ans = INF
    ansa, ansb = a, b
    swap = 0
    if b < a:
        swap = 1
        a, b = b, a
    iter = 0
    for i in range(a, INF):
        j = max(b, ceil(area / i))
        if j * i >= area and j * i <= ans:
            ans = j * i
            ansa = i
            ansb = j
        iter += 1
        if iter >= 100000:
            break
    
    print(ans)
    if swap:
        ansa, ansb = ansb, ansa
    print(ansa, ansb)