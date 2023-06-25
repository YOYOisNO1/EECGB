def program954():
    import math
    import sys
    from sys import stdin, stdout
    
    ipi = lambda: int(stdin.readline())
    ipil = lambda: map(int, stdin.readline().split())
    ipf = lambda: float(stdin.readline())
    ipfl = lambda: map(float, stdin.readline().split())
    ips = lambda: stdin.readline().rstrip()
    out = lambda x: stdout.write(str(x) + "\n")
    outl = lambda x: print(*x)
    
    n = ipi()
    a1, a2, a3 = ipil()
    b1, b2, b3 = ipil()
    
    print(max(0, a1 - b1 - b3) + max(0, a2 - b2 - b1) + max(0, a3 - b3 - b2))
    print(min(a1, b2) + min(a2, b3) + min(a3, b1))