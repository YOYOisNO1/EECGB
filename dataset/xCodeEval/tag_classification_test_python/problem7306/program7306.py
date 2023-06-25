    N, X, Y = map(int, input().split())
    memo = {0: 0, 1: X}
def f(n):
        if n not in memo:
            if n % 2 == 0:
                ans = min(X * n, Y + f(n / 2))
            else:
                ans = min(X * n, X + f(n-1), X + f(n+1))
            memo[n] = ans
        return memo[n]
    print(f(N))