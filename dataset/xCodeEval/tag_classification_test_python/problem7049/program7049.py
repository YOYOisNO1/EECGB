def program7049():
    n = int(input())
    
    cost = 1
    total = 0
    leftover = False
    
    while n > 1 or n == 1 and leftover:
        total += (n / 2) * cost
        if n % 2 == 1:
            if leftover:
                total += cost
                leftover = False
                n += 1
            else:
                leftover = True
        cost *= 2
        n /= 2
    
    print(total)