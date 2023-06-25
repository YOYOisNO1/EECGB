def program4339():
    b,a=map(int,input().split())
    d,c=map(int,input().split())
    vr=-1
    for i in range(500,-1,-1):
        for j in range(500,-1,-1):
            if(a+i*b==c+j*d):
                
                vr=a+i*b
    print(vr)
    
        
            
    
            
                