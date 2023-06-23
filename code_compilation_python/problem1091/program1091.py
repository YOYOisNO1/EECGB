    n = int(input())
def cands():
        xs = set(map(int, input().split()))
        span = max(xs) - min(xs) + 1
        p2 = 1
        while p2 <= span:
            for v in xs:
                yield [w for w in [v - p2, v, v + p2] if w in xs]
            p2 <<= 1
    
    ans = max(cands(), key=len)
    print(len(ans))
    print(*ans, sep=' ')