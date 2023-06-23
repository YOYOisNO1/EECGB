def program756():
    x1,y1,x2,y2,x3,y3=map(float,input().split())
    
    if (x1-x2)**2+(y1-y2)**2==(x2-x3)**2+(y2-y3)**2 and (y2-y1)*(x3-x1)!=(y3-y1)*(x2-x1):
    print('Yes')
    else:
    print('No')