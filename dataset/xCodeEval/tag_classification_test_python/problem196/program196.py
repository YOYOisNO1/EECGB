def program196():
    a,b=map(int,input().split())
    s=str(input())
    count=0
    i=0
    for j in range(1,10000):
        if(s[i]=='1' and i>=a-b-1):
            break
        if(s[i]=='1'):
            i=i+b
            count=count+1
        else:
            i=i-1
    if(s[i]=='1' and i>=a-b-1):
        print(count+1)
    else:
        print(-1)
        
        
                    
                    
    
        
        
        
            
    
            
            
    
    
        
    
        
            
        