def program1618():
    x,y,z=tuple(map(int, input().split()))
    a,b,c=tuple(map(int, input().split()))
    if (x <= a) and (y>= ((a - x ) + b)) and (z>=((a+b+c) - (a-x + a - x + b)):
        print('YES')
    else:
        print('NO')