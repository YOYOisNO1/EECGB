    from collections import defaultdict
    from copy import deepcopy
    
    a = list(input())
    
    d = defaultdict(int)
    for x in a:
        d[int(x)] += 1
    
    
def fact(n):
        ans = 1
        for i in range(1, n + 1):
            ans *= i
        return ans
    
    
    mem = {}
    
    
def f(d):
        n = sum(d.values())
        ans = 0
        if d[0] > 0:
            ans += (n - 1) * fact(n - 1)
        else:
            ans += fact(n)
        for x in d:
            ans //= fact(d[x])
        for k in d:
            if d[k] > 1:
                e = deepcopy(d)
                e[k] -= 1
                ans += f(e)
        mem[frozenset(d.items())] = ans
        return ans
    
    
    ans = f(d)
    print(ans)