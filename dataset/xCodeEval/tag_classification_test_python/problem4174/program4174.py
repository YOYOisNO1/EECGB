def program4174():
    n, a = [int(x) for x in input().split(' ')]
    
    if a % 2 == 0:
        print((n) / 2) + 1 - (a / 2)
    else:
        print((a) + 1) / 2