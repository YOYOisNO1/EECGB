def program411():
    n, m = map(int,input().split())
    p2 = n // 2
    p1 = n % 2
    if (p2 + p1) % m == 0:
        print(p2 + p1)
    '''
    elif p2 == 0 and p1 == n:
        if p1 % 2 == 0:
            print(p1)
        else:
            print('-1')
    '''
    else:
        while True:
            p2 -= 1
            p1 += 2
            if p2 == 0 and p1 == n:
                if p1 % 2 == 0:
                    print(p1)
                    break
                else:
                    print('-1')
                    break
            else:
                (p2 + p1) % m == 0
                print(p2 + p1)
                break