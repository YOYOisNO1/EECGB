def program2929():
    n = int(input())
    
    a = n / 36
    b = (n - a*36) / 3
    if (n - a*36) % 3 == 2:
        b += 1
    
    print '%d %d'%(a, b)