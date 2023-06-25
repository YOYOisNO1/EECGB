def program6168():
    s=input().split()
    x1=int(s[0])
    x2=int(s[2])
    y1=int(s[1])
    y2=int(s[3])
    
    if x1==x2 or y1==y2:
            print(1,)
    else:
            print(2,)
    
    if ((x1%2==0 and y1%2==0) or (x1%2!=0 and y1%2!=0)) and ((x2%2==0 and y2%2==0) or (x2%2!=0 and y2%2!=0)):
    
            if abs(x2-x1) == abs(y2-y1):
                    print(1,)
            else:
                    print(2,)
    
    elif ((x1%2==0 and y1%2!=0) or (x1%2!=0 and y1%2==0)) and ((x2%2==0 and y2%2!=0) or (x2%2!=0 and y2%2==0)):
            if abs(x2-x1) == abs(y2-y1):
                    print(1,)
            else:
                    print(2,)
    else:
            print(0,)
    
    print(max(abs(y2-y1),abs(x2-x1)))