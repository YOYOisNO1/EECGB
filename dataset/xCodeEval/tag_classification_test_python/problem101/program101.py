def program101():
    x,y,z = map(int, input().split())
    a,b,c = map(int, input().split())
    if x <= a:
        if y > a + b - x:
            print('NO')
        else:
            if z <= a + b + c - x - y:
                print('YES')
            else:
                print('NO')
    else:
        print('NO')