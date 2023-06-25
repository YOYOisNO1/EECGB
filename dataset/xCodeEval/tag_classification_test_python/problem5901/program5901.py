    #!/usr/bin/env python3
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visit = [False] * (n + 1)
def gcd(x, y):
        while x != 0:
            y %= x
            if y == 0:
                return x
            x %= y
        return y
def check(u):
        sub = 0
        v = u
        while not visit[v]:
            visit[v] = True
            v = arr[v]
            sub += 1
        if v == u:
            return sub
        return -1
def solve():
        ans = 1
        for i in range(1, n + 1):
            if not visit[i]:
                sub = check(i)
                # print("sub {} i = {}".format(sub, i))
                if sub == -1:
                    return -1
                ans = ans * sub // gcd(ans, sub)
        return ans
    loop = solve()
    if loop == -1:
        print(-1)
    else:
        if loop % 2 == 0:
            loop //= 2
        print(loop)