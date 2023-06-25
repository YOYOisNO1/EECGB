    import sys
    import math
    import bisect
    input=sys.stdin.readline
    from collections import defaultdict
def solve(y):
        return (y*(y+1))//2
    
    for _ in range(int(input())):
        n, k = map(int, input().split())
        ans = 1
        mod = 10**9 + 7
        for i in range(k):
            ans = (ans * n)%mod
        print(ans)
    
        
        