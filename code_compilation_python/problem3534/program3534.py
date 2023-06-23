def program3534():
    inp=input().split()
    for i in range(len(inp)):
        inp[i]=int(inp[i])
    p1=[inp[0],inp[1]]
    p2=[inp[2],inp[3]]
    p3=[inp[4],inp[5]]
    p4=[inp[6],inp[7]]
    if p1[0]>p2[0]:
        atk1=p1[0]
        defe1=p2[1]
    elif p1[0]<p2[0]:
        atk1=p2[0]
        defe1=p1[1]
    else:
        atk1=p1[0]
        defe1=max(p1[1],p2[1])
        
    if atk1>max(p3[0],p4[0]) and defe1>max(p3[1],p4[1]):
        print 'Team 1'
    elif (p3[0]>atk1 and p4[1]>defe1) or (p4[0]>atk1 and p3[1]>defe1):
        print 'Team 2'
    else:
        print 'Draw'