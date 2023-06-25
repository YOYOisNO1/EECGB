def program5336():
    inp = lambda dtype: [dtype(x) for x in input().split()]
    ceil1 = lambda a, b: (a + b - 1) // b
    add = lambda a, b: (a + b) % mod
    mult = lambda a, b: (a * b) % mod
    
    n, mod = inp(int)
    mem, su = [0, 1], 1
    
    for i in range(2, n + 1):
        sq = int(i ** .5) + 1
        mem.append(su)
    
        for f in range(2, sq):
            mem[-1] = add(mem[-1], mem[i // f])
    
        be = i
        for j in range(1, i // sq + 1):
            nxt = i // (j + 1)
            mem[-1] = add(mem[-1], mult(be - nxt, mem[j]))
            be = nxt
    
        su = add(su, mem[-1])
    print(mem[-1])