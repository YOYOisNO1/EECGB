def program6149():
    a = list(map(int, input().split()))
    y1 = a[0]
    d1 = a[1]
    y2 = a[2]
    d2 = a[3]
    yatay = abs(y1 - y2)#0
    dikey = abs(d1 - d2)#1
    a = [0, 0 , 0]
    # kale fil şah
    
    if yatay == 0 or dikey == 0:
        a[0] = 1
    else:
        a[0] = 2
    
    if ((y1+d1) % 2) == ((y2+d2) % 2):
        if yatay == dikey:
            a[1] = 1
        else:
            a[1] = 2
    else:
        a[1] = 0
    
    if yatay == dikey:
        a[2] = yatay
    else:
        a[2] = abs(yatay - dikey) + min(yatay, dikey)
    print(*a)