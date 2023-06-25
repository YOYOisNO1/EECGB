def program3255():
    t1,t2,x1,x2,t0=map(int,input().split())
    
    y1=x1
    y2=x2
    
    z1=0
    z2=0
    mindif=999999999999999
    
    while True: 
        t=1.0*(t1*y1+t2*y2)/(y1+y2)
        if t-t0<mindif and t-t0>=0:
            z1=y1
            z2=y2
            mindif=t-t0
        if y2==0 or y1==0:break
        if(t-t0)>0: 
            y2-=1
        elif (t-t0)<0:y1-=1
        else: break 
    
    print z1,z2
        
        
    
    