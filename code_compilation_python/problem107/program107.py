def program107():
    import math
    a = [int(i) for i in input().split()]
    z = -1
    
    for i in range(a[1]-a[0]):
        k = i+a[0]
        if math.gcd(a[0],k)==1 and math.gcd(a[1], k)==1:
            z = k
            break
    
    print(str(a[0]) + ' ' + str(z) + ' ' + str(a[1]))