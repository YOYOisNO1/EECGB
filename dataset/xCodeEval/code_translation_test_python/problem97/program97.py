    from sys import stdin, setrecursionlimit
    from collections import *
    from types import GeneratorType
    
    # setrecursionlimit(200000)
    add = lambda a, b: (a % mod + b % mod) % mod
    rints, mod = lambda: [int(x) for x in stdin.readline().split()], 100000000
    
    
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
            if stack:
                return f(*args, **kwargs)
            else:
                to = f(*args, **kwargs)
                while True:
                    if type(to) is GeneratorType:
                        stack.append(to)
                        to = next(to)
                    else:
                        stack.pop()
                        if not stack:
                            break
                        to = stack[-1].send(to)
                return to
    
        return wrappedfunc
    
    
    @bootstrap
def dp(i1, i2, j, k):
        if i1 + i2 >= n1 + n2:
            yield 1
    
        # print(i1, i2, j, k)
        if mem[i1][i2][j][k] != -1:
            yield mem[i1][i2][j][k]
    
        mem[i1][i2][j][k] = 0
        if i1 < n1:
            if j != 0:
                t = yield dp(i1 + 1, i2, 0, 1)
                mem[i1][i2][j][k] = add(mem[i1][i2][j][k], t)
    
            elif k < k1:
                t = yield dp(i1 + 1, i2, 0, k + 1)
                mem[i1][i2][j][k] = add(mem[i1][i2][j][k], t)
    
        if i2 < n2:
            if j != 1:
                t = yield dp(i1, i2 + 1, 1, 1)
                mem[i1][i2][j][k] = add(mem[i1][i2][j][k], t)
    
            elif k < k2:
                t = yield dp(i1, i2 + 1, 1, k + 1)
                mem[i1][i2][j][k] = add(mem[i1][i2][j][k], t)
    
        yield mem[i1][i2][j][k]
    
    
    n1, n2, k1, k2 = rints()
    mem = [[[[-1 for _ in range(11)] for _ in range(3)] for _ in range(101)] for _ in range(101)]
    print(dp(0, 0, 2, 0))