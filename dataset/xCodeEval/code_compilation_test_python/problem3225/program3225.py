def program3225():
    k, a, b = map(int, input().split())
    
    aa, bb = a / k, b / k
    if aa == 0 && b % k != 0:
        print -1
    elif bb == 0 && a % k != 0:
        print -1
    else:
        print aa + bb