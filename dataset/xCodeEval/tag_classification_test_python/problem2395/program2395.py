def program2395():
    from sys import stdin
    
    n = stdin.readline().rstrip()
    count4, count7 = n.count('4'), n.count('7')
    
    if count4 >= count7 and count4 > 0:
        print(4)
    elif count7 >= count4 and count7 > 0:
        print(7)
    else:
        print(-1)