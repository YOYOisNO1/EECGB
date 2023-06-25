    p0 = tuple(map(int, input().split()))
    p1 = tuple(map(int, input().split()))
    p2 = tuple(map(int, input().split()))
    
def rev(t):
        return (t[1], t[0])
    
def solve(a, b, c):
        return solve2(a, b, c) or solve2(rev(a), b, c)
    
def solve2(a, b, c):
        return solve3(a, b, c) or solve3(a, rev(b), c)
    
def solve3(a, b, c):
        return solve4(a, b, c) or solve4(a, b, rev(c))
    
def solve4(a, b, c):
        return a[0] >= b[0] + c[0] and a[1] >= max(b[1], c[1])
    
    print("YES" if solve(p0, p1, p2) else "NO")