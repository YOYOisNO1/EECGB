def program2997():
    x1,y1,x2,y2=map(int, input().split())
    if x1+y1 <= max(x2,y2) or (x1 <= y1 and x2 <= y2): print "Polycarp"
    else: print "Vasiliy"