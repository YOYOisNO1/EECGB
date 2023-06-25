def program1467():
    a, b, c = map(int, input().split())
    sum = a+b+c
    if(sum % 2 == 0):
        sum //= 2
        x, y, z = sum - c, sum - a, sum - b
        if(x >= 0 and y >= 0 and z >= 0):
            print(x, y, z)
        else:
            print('Impossible')
    else:
        print('Impossible')