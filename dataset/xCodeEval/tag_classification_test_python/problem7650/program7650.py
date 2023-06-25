    import sys
    from array import array  # noqa: F401
    
    
def input():
        return sys.stdin.buffer.readline().decode('utf-8')
    
    
    k = int(input())
    R = 4 * k**2
    
    
def judge(x, y, c):
        if x & 1:
            return (
                c >= 12 * y**2 + 24 * y + 12
                and c >= 6 * x + 12 * y**2 + 12 * y + 3
            )
        else:
            return (
                c >= 12 * y**2 + 12 * y + 3
                and c >= 6 * x + 12 * y**2
            )
    
    
def solve(x):
        c = R - (9 * x**2 + 6 * x + 1)
        ok, ng = -1, 10**6
        while abs(ok - ng) > 1:
            y = (ok + ng) >> 1
            if judge(x, y, c):
                ok = y
            else:
                ng = y
        return ok
    
    
    y = solve(0)
    if y == -1:
        print(0)
        exit()
    
    
    ans = 1 + y * 2
    for x in range(1, k):
        y += 1
        c = R - (9 * x**2 + 6 * x + 1)
        if x & 1:
            while y >= 0 and not judge(x, y, c):
                y -= 1
        else:
            while y >= 0 and not judge(x, y, c):
                y -= 1
        if y < 0:
            break
        ans += ((y + 1) * 2 if x & 1 else 1 + y * 2) * 2
    
    print(ans)