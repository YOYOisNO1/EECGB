def program4819():
    l, r = map(int, input().split())
    k1 = 1
    num1 = 0
    while k1 <= r:
        k2 = k1
        while k2 <= r:
            k2 *= 3
            num1 += 1
        k1 *= 2
    
    k1 = 1
    num2 = 0
    while k1 < l:
        k2 = k1
        while k2 < l:
            k2 *= 3
            num2 += 1
        k1 *= 2
    
    
    print(num1 - num2)