def cnt(n):
        res = 0
        while n:
            n >>= 1
            res += 1
        return res
def cal(n, i, c):
        if i == (1<<c):
            return n&1
        elif i < (1<<c):
            return cal(n//2, i, c-1)
        else:
            return cal(n//2, i - (1<<c), c-1)
    n, l, r = map(int, input().split())
    ans = 0
    c = cnt(n)
    if n>0:
        for i in range(l, r + 1):
            if cal(n, i, c-1):
                ans += 1
    print(ans)