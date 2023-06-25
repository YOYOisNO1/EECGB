def program6156():
    x1,y1,x2,y2=list(map(int,input().split()))
    a,b,c=0,0,0
    
    if x1==x2 or y1==y2:
        a=1
    else:
        a=2
        
    c=max(abs(x1-x2),abs(y1-y2))
    if (abs(x1-x2)+abs(y1-y2))%2!=0:
        b=0
    else:
        if abs(x1-x2)==abs(y1-y2):
            b=1
        else:
            b=2
    print(a,b,c)
    