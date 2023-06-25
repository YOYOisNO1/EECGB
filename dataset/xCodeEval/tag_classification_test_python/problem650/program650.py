def program650():
    R=lambda:map(int,input().split())
    a1,b1,c1=R()
    a2,b2,c2=R()
    Z=lambda x,y,z:not x and not y and z
    if a1*b2-a2*b1!=0:  print("1")
    elif Z(a1,b1,c1) or Z(a2,b2,c2) or c1*b2-b1*c2 or c1*a2-c2*a1:    print("0")
    else:   print("-1")