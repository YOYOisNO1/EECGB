def program434():
    import math
    
    primeira_entrada = input().split()
    a1 = int(primeira_entrada[0])
    a2 = int(primeira_entrada[1])
    a3 = int(primeira_entrada[2])
    
    cups = a1 + a2 + a3
    
    segunda_entrada = input().split()
    b1 = int(segunda_entrada[0])
    b2 = int(segunda_entrada[1])
    b3 = int(segunda_entrada[2])
    
    medals = b1 + b2 + b3
    
    n = int(input())
    
    n = n - (math.ceil(cups / 5.0))
    n = n - (math.ceil(medals / 10.0))
    
    if n < 0:
        print('NO')
    else:
        print('YES')