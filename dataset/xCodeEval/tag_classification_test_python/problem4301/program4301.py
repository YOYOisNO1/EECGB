def program4301():
    import sys
    import math
    input=sys.stdin.readline
    
    w=list(map(int,input().split()))
    b1=list(map(int,input().split()))
    b2=list(map(int,input().split()))
    x1=max(w[0],b1[0])
    x2=min(w[2],b1[2])
    y1=max(w[1],b1[1])
    y2=min(w[3],b1[3])
    x3=max(w[0],b2[0])
    x4=min(w[2],b2[2])
    y3=max(w[1],b2[1])
    y4=min(w[3],b2[3])
    xa=max(x1,x3)
    
    xb=min(x2,x4)
    ya=max(y1,y3)
    yb=min(y2,y4)
    
    ans=(w[3]-w[1])*(w[2]-w[0])
    if(x2>=x1 and y2>=y1):
        ans-=(x2-x1)*(y2-y1)
    if(xb>=xa and yb>=ya):
        ans+=(xb-xa)*(yb-ya)
    if(x4>=x3 and y4>=y3):
        ans-=(x4-x3)*(y4-y3)
    
    if(ans>0):
        print("YES")
    else:
        print("NO")
    
            
        
    
                
        
        
                
    
        
        
            
        
        