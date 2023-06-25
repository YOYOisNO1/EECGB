def program1199():
    a = [input() for i in range(3)]
    b = [a[0][i] + a[1][i] + a[2][i] for i in range(3)]
    c = [a[0][0] + a[1][1] + a[2][2], a[0][2] + a[1][1] + a[2][0]] 
    t = a + b + c
    
    x = sum(i.count('X') for i in a)
    y = sum(i.count('0') for i in a)
    if x == y + 1: k = 1
    elif x == y: k = 0
    else: k = 2
    
    if k < 2:
        if '000' in t:
            if 'XXX' in t: k = 2
            elif k == 0: k = 4
            else: k = 2
        elif 'XXX' in t:
            if k == 1: k = 3
            else: k = 2
        elif not any('.' in i for i in a): k = 5
        
    print(['first', 'second', 'illegal', 'the first player won', 'the second player won', 'draw'][k])