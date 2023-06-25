def program2999():
    xp, yp, xv, yv = map(int, input().split())
    
    if xp<=xv and yp<=yv:
        print "Polycarp"
    else:
        print "Vasiliy"