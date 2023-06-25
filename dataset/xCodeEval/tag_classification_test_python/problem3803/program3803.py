def program3803():
    n, bx = list(map(int, input().split(' ')))
    x = list(map(int, input().split(' ')))
    n, by = list(map(int, input().split(' ')))
    y = list(map(int, input().split(' ')))
    x.reverse()
    y.reverse()
    k = 1
    X = 0
    for i in x:
        X += i * k
        k *= bx
    Y = 0
    k = 1
    for i in y:
        Y += i * k
        k *= by
    if X<Y:
        print('<')
    elif X>Y:
        print('>')
    else :
        print('=')