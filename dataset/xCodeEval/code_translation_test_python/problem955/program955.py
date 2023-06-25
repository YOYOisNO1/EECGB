def program955():
    dt = {0 : 6, 1 : 2, 2 : 5, 3 : 5, 4 : 4, 5 : 5, 6 : 6, 7 : 3, 8 : 7, 9 : 6}
    a, b = map(int, input().split())
    print( sum( sum( dt[ int(ni) ] for ni in str(n) ) for n in range(a, b + 1) ) )