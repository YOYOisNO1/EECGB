def program467():
    mas = sorted(list(map(int, input().split()))
    if mas[0] + mas[1] > mas[2] or mas[0] + mas[1] > mas[3]:
        print('TRIANGLE')
    elif mas[0] + mas[1] == mas[2] or mas[0] + mas[1] == mas[3]:
        print('SEGMENT')
    else:
        print('IMPOSSIBLE')