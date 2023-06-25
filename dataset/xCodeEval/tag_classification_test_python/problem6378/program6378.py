def program6378():
    k = tuple(sorted(map(int, input().split())))
    
    if 1 in k or k.count(2) > 1 or k.count(3) == 3 or k == (2, 4, 4):
        print('YES')
    else:
        print('NO')