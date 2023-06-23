def program1724():
    
    x, y, z = map(int, input().split())
    
    if x == y == z ==0:
        print('0')
    elif abs(x-y) > z:
        if x > y:
            print('+')
        elif x < y:
            print('-')
        else:
            print('0')
    elif abs(x -y) ==z:
        if not z:
            print('0')
        else:
            print('?’)
    else:
        print('?')