def program1029():
    n = int(input())
    x, y, z, = [int(i) for i in input().split()]
    a, b, c =  [int(i) for i in input().split()]
    
    a, b, c = b, c, a
    
    mi = max(0, max(x - b - c, max(y - a - c, z - a - b)))
    ma = min(x, a) + min(y, b) + min(z, c)
    print(mi, ma)