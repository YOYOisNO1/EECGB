    import math
    
def node(a, b):
        while (b > 0):
            c = a % b
            a = b
            b = c
        return a
    
    a = map(int, input().split())
    b = max(a[0], a[1])
    c = 6 - b + 1
    d = node(c, 6)
    print(("%d/%d") % ( (c // d), 6 // d ) )