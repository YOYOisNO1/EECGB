def program2286():
    [x, y, z, t1, t2, t3] = [int(n) for n in input().split()]
    print('YES' if (abs(x-y)*t1 > 3*t3 + (abs(x-z)+abs(x-y))*t2) 'NO')