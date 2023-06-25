def solve(num, p):
        return True if num == 0 else False if num >= p * 2 else solve(min(num, abs(p - num)), p // m)
    m, num = map(int, input().split())
    p = 1
    while p < num: p *= m
    print("YES" if solve(num, p) else "NO")