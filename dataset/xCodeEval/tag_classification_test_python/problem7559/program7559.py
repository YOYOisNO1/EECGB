def program7559():
    
    
    n, m, k = map(int, input().split())
    
    if n % 2:
        if k == 1:
            if m == 1:
                print('Marsel')
            else:
                print('Timur')
        else:
            d = 2
            ok = False
            while d * d <= m:
                if m % d == 0:
                    if m / d >= k:
                        ok = True
                    break
                d += 1
    
            if ok:
                print('Timur')
            else:
                print('Marsel')
    else:
        print('Marsel')