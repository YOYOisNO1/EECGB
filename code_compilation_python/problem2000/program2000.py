def program2000():
    Vertical = []
    Horizontal = []
    check = True
    for i in range(0,4):
        T = [int(x) for x in input().split()]
        if (T[0] == T[2] and T[1] == T[3]):
            check = False
        elif (T[0]== T[2]):
            Vertical.append(T)
        elif (T[1] == T[3]):
            Horizontal.append(T)
        else:
            check = False
    
    if len(Vertical) == 2:
        if len(Horizontal) == 2:
            VC1 = (Vertical[0][1] == Vertical[1][1] or Vertical[0][1] == Vertical[1][3])
            VC2 = (Vertical[0][3] == Vertical[1][1] or Vertical[0][3] == Vertical[1][3])
            
            HC1 = (Horizontal[0][0] == Horizontal[1][0] or Horizontal[0][0] == Horizontal[1][2])
            HC2 = (Horizontal[0][2] == Horizontal[1][0] or Horizontal[0][2] == Horizontal[1][2])
    
    else:
        VC1 = 0
        VC2 = 0
        HC1 = 0
        HC2 = 0
    VV = set()
    HV = set()
    for i in Vertical:
        VV.add((i[0],i[1]))
        VV.add((i[2],i[3]))
    
    
    for i in Horizontal:
        for j in i:
            HV.add((i[0],i[1]))
            HV.add((i[2],i[3]))
            
    FinalCheck = VV == HV
    if check*FinalCheck*VC1*VC2*HC1*HC2:
        print('YES')
    else:
        print('NO')
        