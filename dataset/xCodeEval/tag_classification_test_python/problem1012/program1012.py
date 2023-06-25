def program1012():
    ##rock-a1
    ##scissor-a2
    ##paper-a3
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ma=0
    ##max
    ma+=min(a[0],b[1])
    ma+=min(a[1],b[2])
    ma+=min(a[2],b[0])
    ##min
    m=min(a[0],b[2])
    a[0]-=min(a[0],b[0]+b[2])
    a[1]-=min(a[1],b[1]+b[0])
    a[2]-=min(a[2],b[1]+b[2])
    print(sum(a),ma)
        
    
    
                
        
            