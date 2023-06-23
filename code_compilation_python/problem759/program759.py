def program759():
    x1,y1,x2,y2,x3,y3 = map(int,input().split())
    
    if(abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)0)>0):
        if(((x2-x1)**2+(y2-y1)**2)  ==  ((x3-x2)**2+(y3-y2)**2)):
            print("Yes")
        else:
            print("No")
    else:
        print("No")