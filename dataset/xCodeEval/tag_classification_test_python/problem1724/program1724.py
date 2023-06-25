def program1724():
    s = input().split()
    (x, y, z) = (int(s[0]), int(s[1]), int(s[2]))
    
    if x > y:
        tmp = x
        x = y
        y = tmp
    
    if y >= z:
        print(0)
    elif y <= 0:
        print(-1)
    else:
        r = 0
        a = 0
        b = 1
        if x < 0:
            if x % y:
                r = (-x/y)+1
                x = r*y + x
            else:
                r = -x/y
                x = 0
        while (a*x + b*y) < z:
            c = b
            b = a+b
            a = c
            r += 1
        print(r)
    
    #s = input()
    
    #i = 0
    #h = 0
    #r = 0
    #while i < (len(s)-4):
    #    if (s[i:i+5] == 'heavy'):
    #        h += 1
    #        i += 4
    #    elif (s[i:i+5] == 'metal'):
    #        r += h
    #        i += 4
    #    i += 1
    
    #print(r)
    
    #s = input()
    #s1 = s.split()
    #n = int(s1[0])
    #k = int(s1[1])
    
    #b = n/2 + (n%2)
    
    #if k <= b:
    #    print(k*2-1)
    #else:
    #    print((k-b)*2)
    