def program1691():
     a='v<^>'
    q,w=(str(i) for i in input().split())
    k=int(input())%4
    a1=a.find(q)
    a2=a.find(w)
    f1=False
    f2=False
    f3=False
    f4=False
    If (a1==a2) and (k==0):
        print('undefined')
    else:
        if a1<=a2:
            if abs(a2-a1)==k:
                f1=True
            if 4-abs(a2-a1)==k:
                f2=True
        else:
            if a1-a2==k:
                f3=True
            if 4-a1+a2==k:
                f4=True
        if ((f1) and (f2)) or ((f3) and (f4)):
            print('undefined')
        elif (f1) or (f4):
            print('cw')
        elif (f2) or(f3):
            print('ccw')