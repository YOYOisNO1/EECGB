def program14():
    n, s = [int(x) for x in input().split(' ')]
    a = sorted([int(x) for x in input().split(' ')])
    if sum(a[:n-1]) <= s: print('YES')
    else: print('NO')