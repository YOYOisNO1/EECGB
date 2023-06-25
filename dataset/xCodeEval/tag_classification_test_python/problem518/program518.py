def program518():
    a = input()
    a = a.split(' ')
    
    n, m, a = int(a[0]), int(a[1]), int(a[2])
    
    n, y = divmod(n, a)
    if y > 0: n += 1
    
    m, y = divmod(m, a)
    if y > 0: m += 1
    
    print(m) * n