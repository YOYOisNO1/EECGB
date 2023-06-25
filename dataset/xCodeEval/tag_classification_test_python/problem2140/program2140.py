def program2140():
    from sys import stdin
    input = stdin.readline
    
    n = int(input())
    
    res = 0
    
    while n >= 10:
        n += 1
        while n % 10 == 0:
            n //= 10
        res += 1
        
    print(res+9)