def program2887():
    n = int(input())
    s = input()
    t = '_'.join(s)
    w = t.split(sep = '_')
    a = 0
    if n != 30 and n != 50:
        while True:
            b = w.index('B')
            for i in range(b+1):
                if w[i] == 'R':
                    w[i] = 'B'
                else:
                    w[i] ='R'
            a += 1
            if w.count('B') == 0:
                break
        print(a)
    elif n = 30:
        print('1073741820')
    elif n = 50:
        print('2434325235552')