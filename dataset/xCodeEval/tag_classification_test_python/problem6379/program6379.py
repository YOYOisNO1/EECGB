def program6379():
    k = list(map(int, input().split()))
    k.sort()
    if k.count(2) > 1 or k.count(1) > 0 or k == [2,4,4] or k == [3,3,3]:
        print('YES')
    else:
        print('NO')