def program5303():
    inp = lambda dtype: [dtype(x) for x in input().split()]
    ceil1 = lambda a, b: (a + b - 1) // b
    add = lambda a, b: (a + b) % mod
    mult = lambda a, b: (a * b) % mod
    
    n, mod = inp(int)
    mem, prefix = [0] * (n + 1), [0] * (n + 2)
    mem[1] = su = 1
    
    for i in range(2, n + 1):
        j = 2
        while j * (i - 1) <= n:
            prefix[j * (i - 1)] = add(prefix[j * (i - 1)], mem[i - 1])
            prefix[min(j * i, n + 1)] = add(prefix[min(j * i, n + 1)], mult(-1, mem[i - 1]))
            j += 1
    
        prefix[i] = add(prefix[i - 1], prefix[i])
        mem[i] = add(prefix[i], su)
        su = add(su, mem[i])
    
    print(mem[-1])