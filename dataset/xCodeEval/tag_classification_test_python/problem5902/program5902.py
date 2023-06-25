    from sys import stdin
    from fractions import gcd
    from functools import reduce
    
    rints = lambda: [int(x) for x in stdin.readline().split()]
    lcm = lambda a, b: a // gcd(a, b) * b
    
    
def dfs(x):
        x1 = a[x - 1]
        visit, c = [0] * (n + 1), 1
        visit[x] = 1
    
        while x1 != x:
            visit[x1] = 1
            x1 = a[x1 - 1]
            if visit[x1] and x1 != x:
                return -1
            c += 1
    
        return c
    
    
    n, a, ans = int(input()), rints(), []
    
    for i in range(n):
        val = dfs(i + 1)
        if val == -1:
            print(-1)
            exit()
        else:
            ans.append(val if val % 2 else val // 2)
    
    print(reduce(lcm, ans))