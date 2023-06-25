def f(n):
        if n <= 1:
            return n
        return 2 * f(n // 2) + n % 2
    
def g(n):
        if n <= 1:
            return 1
        return 2 * g(n // 2) + 1
        
def solve(n, x):
        global ans
        if x == 0:
            return
        a1 = n // 2
        a2 = n % 2
        if n <= 1:
            if x == 0:
                return
            else:
                ans = n
                return
        c = g(a1)
        if x < c:
            solve(a1, x)
            return
        if x == c:
            ans += f(a1)
            return
        ans += f(a1)
        
        x -= g(a1)
        if x == 1:
            ans += a2
            return
        ans += a2
        x -= 1
        
        if x == c:
            ans += f(a1)
            return
        solve(a1, x)
    
    n, l, r = map(int, input().split())
    ans = 0
    solve(n, l - 1)
    l = ans
    ans = 0
    solve(n, r)
    r = ans
    print(r - l)