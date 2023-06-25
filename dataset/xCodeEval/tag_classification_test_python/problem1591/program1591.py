def program1591():
    x = [int(s) for s in input().split(' ')]
    i = 0
    while x[i % 2] > i:
        x[i % 2] -= (i + 1)
        i += 1
    if i % 2 == 0:
        print('Vladik')
    else:
        print('Valera')