def program57():
    x, y = input().split('.')
    l = y.split('e')
    l.append(x)
    d, b, a = map(str, l)
       
    if d == '0':
        d = '' + '0' * int(b)
    elif int(b) == len(d):
        ans = a + d
    elif int(b) > len(d):
        d = d + '0' * (int(b) - len(d))
    else:
        d = d[0:int(b)] + '.' + d[int(b):]
        
    ans = a + d
        
    print(ans)