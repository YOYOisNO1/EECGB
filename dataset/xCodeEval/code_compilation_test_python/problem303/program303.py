def program303():
    a = []
    a.append(input())
    a.append(input())
    a.append(input())
    a.append(input())
    b = []
    
    for i in range(len(a)):
        b.append(len(a[i]) - 2)
    
    b.sort()
    
    res = 0
    
    if b[0] * 2 <= b[1] and b[1] != 0:
        res = b[0]
    elif b[2] * 2 <= b[3] and b[3] != 0:
        res = b[3]
    
    if res != 0:
        for i in range(len(a)):
            if len(a[i]) - 2 == res:
                print(a[i][:1])
    else:
        print('C')