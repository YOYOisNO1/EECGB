def program317():
    r = input().split(' ')
    
    a = int(r[0])
    b = int(r[1])
    c = int(r[2])
    d = int(r[3])
    
    misha = max (3 * a, a - (a * c /250)) 
    vasya = max (3 * b, b - (b * d /250))
    
    if misha > vasya:
        print "Misha"
    
    elif misha < vasya:
        print "Vasya"
    
    else:
        print "Tie"