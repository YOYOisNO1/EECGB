def solve(n, s):
        cur = -1
        for i in xrange(s, n + 1):
            ds = sum(map(int, str(i)))
            if i - ds >= s:
                cur = i
                break
        if cur == -1:
            return 0
        return n - cur + 1
        
    assert solve(12, 1) == 3
    assert solve(25, 20) == 0
    assert solve(10, 9) == 1
    
    
    (n, s) = map(int, input().split())
    print solve(n, s)