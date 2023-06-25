def program1208():
    n = input()
    com = input()
    count=0
    d = {'L':0, 'D':0, 'U':0, 'R':0}
    for i in com:
        if i=='L':
            d['L']+=1
        elif i=='D':
            d['D']+=1
        elif i=='U':
            d['U']+=1
        else:
            d['R']+=1
    if d['L']==d['U']==d['R']==d['D']:
        count =n
    else:
        if d['L']==d['R']:
            count = 2*min(d['U'],d['D'])+2*d['L']
        elif d['U']==d['D']:
            count = 2*min(d['L'],d['R'])+2*d['U']
        else:
            count = 2*min(d['U'],d['D']) + 2*min(d['L'],d['R'])
    print(count)