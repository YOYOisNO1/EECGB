def program3579():
    n, t = map(int, input().split(' '))
    f = input()
    lst = []
    for i in range(len(f)):
        lst += f[i]
    for j in range(t):
        k = 0
        if len(lst) >= 2:
            ajk = lst[-2]
            if ajk == 'B' and lst[-1] == 'G':
                lst[-2] == 'G'
                lst[-1] == 'B'
        while k < n-1:
            if lst[k] == 'B' and lst[k+1] == 'G':
                lst[k] = 'G'
                lst[k+1] = 'B'
                k += 2
            else:
                k += 1
    
    s = ''
    for l in range(len(lst)):
        s += lst[l]
    print(s)