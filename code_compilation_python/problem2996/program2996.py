def program2996():
    string = input()
    string = string.split()
    xP = int(string[0])
    yP = int(string[1])
    xV = int(string[0])
    yV = int(string[1])
    
    #print xP, yP, xV, yV
    
    Pwin = xP + yP
    Vwin = min(xV, yV)
    
    if (xP + 1) * 2 >= xV + 1 or (yP + 1) * 2 >= yV + 1:
        print 'Polycarp'
    elif xP <= xV and yP <= yV:
        print 'Polycarp'
    else:
        print 'Vasiliy'