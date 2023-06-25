def program2290():
    n = input()
    l = len(n)
    for i in range(l-1,-1,-1):
        a = int(n[i])
        x = ['O']*2
        y = ['O']*5
        if(a<5):
            x[1] = '-'
            y[a] = '-'
        else:
            x[0] = '-'
            y[a%5] = '-'
        x = ''.join(x)
        y = ''.join(y)
        print(x + '|' + y)