def program6023():
    # -*- coding: utf-8 -*-
    a, b = map(int, input().split(' '))
    
    win = 0
    draw = 0
    lose = 0
    for i in xrange(1, 7):
        if abs(a - i) < abs(b - i):
            win += 1
        elif abs(a - i) == abs(b - i):
            draw += 1
        elif abs(a - i) > abs(b - i):
            lose += 1
    
    print('{} {} {}'.format(win, draw, lose))