def program1452():
    n = int(input())
    x = [int(s) for s in input().split(' ')]
    y = [int(s) for s in input().split(' ')]
    z = set(x).union(set(y))
    cnt = 0
    for a in x:
        for b in y:
            if a^b in z:
                cnt += 1
    if cnt % 2 == 0:
        print('Karen')
    else:
        print('Koyomi')