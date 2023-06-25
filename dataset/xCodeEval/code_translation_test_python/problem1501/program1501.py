def inp():
        return map(int, stdin.readline().split())
    
    
def factorize(n):  # o(sqr(n))
        c, ans = 1, 0
        while (c * c < n):
            if n % c == 0:
                ans += 2
            c += 1
    
        if c * c == n:
            ans += 1
        return ans
    
    
    from sys import *
    from collections import *
    
    a, b, c = inp()
    mem, ans = defaultdict(int), 0
    
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                pro = i * j * k
                if mem[pro] == 0:
                    mem[pro] = factorize(pro)
                ans += mem[pro]
    print(ans)