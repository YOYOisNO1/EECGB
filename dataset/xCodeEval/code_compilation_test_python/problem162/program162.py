def program162():
    da, db = map(int, input().split())
    if da == 9 and db == 1:
        print('999 1000')
    elif da > db:
        print(-1)
    elif da == 0:
        print(-1)
    elif da == db:
        print('{}00 {}01'.format(da, da))
    elif da == 9 and db == 1:
        print('999 1000')
    elif da + 1 == db:
        print('{}99 {}00'.format(da, db))
    else:
        print(-1)