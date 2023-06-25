    #!/usr/bin/python2
    from sys   import *
    from os    import *
    from math  import *
    from heapq import *
    
def solve():
    def read(fn = int):
            return list(map(fn, input().split()))
    def mask(num):
            try:
                return int(''.join([c for c in str(num) if c in ('4', '7')]))
            except ValueError:
                return 0
        a, b = input().split()
        a = int(a) + 1
        b = int(b)
        while mask(a) != b:
            a += 1
        print(a)
    solve()