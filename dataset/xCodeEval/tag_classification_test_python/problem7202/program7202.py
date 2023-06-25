    
    [n, k, l, m] = map(int, input().split())
    
def fibo(n, m):
    def power(a, n):
            r = [[0 for x in range(2)] for x in range(2)]
            r[0][0] = 1
            r[0][1] = 0
            r[1][0] = 0
            r[1][1] = 1
            while n > 0:
                if n % 2:
                    r = mul(r, a)
                a = mul(a, a)
                n = n / 2
            return r
    def mul(a, b):
            c = [[0 for x in range(2)] for x in range(2)]
            for i in range(0, 2):
                for j in range(0, 2):
                    for k in range(0, 2):
                        c[i][j] = c[i][j] + a[i][k] * b[k][j]
                        c[i][j] = c[i][j] % m
            return c
        a = [[0 for x in range(2)] for x in range(2)]
        a[0][0] = 0
        a[0][1] = 1
        a[1][0] = 1
        a[1][1] = 1
        r = [[0 for x in range(2)] for x in range(2)]
        r = power(a, n)
        return r[1][1]
    
    if k >= 2 ** l or m == 1:
        print(0)
    else:
        ans = 1
        for i in range(l):
            if not k & (1 << i):
                now = fibo(n + 1, m) % m
            else:
                now = (pow(2, n, m) - fibo(n + 1, m)) % m
                if now < 0:
                    now = now + m
            ans = ans * now
            ans = ans % m
        print(ans)