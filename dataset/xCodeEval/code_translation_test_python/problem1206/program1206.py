def program1206():
    a = input().split()
    x = int(a[0])
    y = int(a[1])
    z = abs(x) + abs(y)
    if x > 0:
        print('0 ') + str(z*y/abs(y)) + " " + str(z*x/abs(x)) + ' 0'
    else:
        print(str(z*x/abs(x))) + ' 0 0 ' + str(z*y/abs(y))