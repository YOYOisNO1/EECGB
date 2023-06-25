    #!/usr/bin/python3
    
    from itertools import permutations
    
def ap(t, p):
        return [t[q] for q in p]
    
    n, k = map(int, input().split())
    s = [input() for i in range(n)]
    ans = 10 ** 100
    for p in permutations(range(k)):
        u = [int(''.join(ap(t, p))) for t in s]
        ans = min(ans, max(u) - min(u))
    print(ans)