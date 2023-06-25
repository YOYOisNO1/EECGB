def program3047():
    import math
    
    a, b = [int(i) for i in input().split()]
    z = -1
    otv=str()
    
    for i in range(a, b-1):
        for n in range(i, b):
            for g in range(n, b+1):
                if math.gcd(i, n) == 1 and math.gcd(n, g) == 1 and math.gcd(g,i) != 1:
                    z=1
                    otv=(str(i) + ' ' + str(n) + ' ' + str(g))
                    break
            if z==1:
                break
        if z==1:
            break
    
    if z == -1:
        print(z)
    else:
        print(otv)