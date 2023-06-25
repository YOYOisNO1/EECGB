    import sys
    input = sys.stdin.readline
    
    
    
def make_tree(n):
        i = 2
        while True:
            if i >= n * 2:
                tree = [0] * i
                break
            else:
                i *= 2
        return tree
    
def update(i, x):
        i += len(tree) // 2
        tree[i] = x
        i //= 2
        while True:
            if i == 0:
                break
            tree[i] = tree[2 * i] + tree[2 * i + 1]
            i //= 2
        return
    
def get_sum(s, t):
        s += len(tree) // 2
        t += len(tree) // 2
        ans = 0
        while True:
            if s > t:
                break
            if s % 2 == 0:
                s //= 2
            else:
                ans += tree[s]
                s = (s + 1) // 2
            if t % 2 == 1:
                t //= 2
            else:
                ans += tree[t]
                t = (t - 1) // 2
        return ans
    
def prime_factorize(n):
        ans = []
        for i in range(2, int(n ** (1 / 2)) + 1):
            while True:
                if n % i:
                    break
                ans.append(i)
                n //= i
            if n == 1:
                break
        if not n == 1:
            ans.append(n)
        return ans
    
def euler_func(n):
        p = set(prime_factorize(n))
        x = n
        for i in p:
            x *= (i - 1)
            x //= i
        return x
    
def f(a, b):
        ans = 1
        for i in range(a + 1, b + 1):
            ans *= i
            ans %= mod
        return ans
    
    n, mod = map(int, input().split())
    x = euler_func(mod)
    l = n + 5
    fact = [1] * (l + 1)
    for i in range(1, l + 1):
        fact[i] = i * fact[i - 1] % mod
    if n <= 3:
        ans = 0
    else:
        dp = [0] * 2000
        dp[0], dp[1], dp[2], dp[3] = 1, 2, 2, 1
        tree = make_tree(2005)
        for i in range(4):
            update(i, dp[i])
        m = 3
        ans = 0
        for i in range(n - 3):
            dp0 = list(dp)
            ans0 = 0
            for j in range(i + 3):
                for k in range(1, m + 2):
                    ans0 += get_sum(j + k + 1, 2004) * dp0[k - 1] % mod
                    ans0 %= mod
                    dp[j + k] += dp0[k - 1]
                    dp[j + k] %= mod
                    update(j + k, dp[j + k])
            m += i + 3
            ans += f(i + 4, n) * ans0 % mod
            ans %= mod
    print(ans)