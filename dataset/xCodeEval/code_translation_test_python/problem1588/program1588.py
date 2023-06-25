def program1588():
    from math import sqrt
    
    inp = lambda dtype: [dtype(x) for x in input().split()]
    ceil1 = lambda a, b: (a + b - 1) // b
    add = lambda a, b: (a + b) % mod
    mult = lambda a, b: (a * b) % mod
    
    n, mod = inp(int)
    mem, su = [0] * (n + 1), 1
    mem[1] = 1
    
    for i in range(2, n + 1):
        sq, cur = int(sqrt(i)) + 1, su
    
        for f in range(2, sq):
            cur = (cur + mem[i // f]) % mod
    
        be = i
        for j in range(1, i // sq + 1):
            nxt = i // (j + 1)
            cur = (cur + (be - nxt) * mem[j]) % mod
            be = nxt
    
        su = (su + cur) % mod
        mem[i] = cur
    print(mem[-1])