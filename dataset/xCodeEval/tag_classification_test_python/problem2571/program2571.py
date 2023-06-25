def program2571():
    n, a, x, b, y = map(int, input().split(' '))
    
    d = int()
    if a < b:
        d = b - a
    else:
        d = n - a + b
    boo = (d % 2) == 0
    
    k1 = int()
    if a < x:
        k1 = x - a
    else:
        k1 = n - a + x
    
    k2 = int()
    if b > y:
        k2 = b - y
    else:
        k2 = n - y + b
    
    if not boo and n % 2 == 1:
        if (d + n)/2 <= min(k1, k2):
            boo = True
    
    if d/2 > min(k1, k2):
        boo = False
    
    if boo:
        print('Yes')
    else:
        print('No')