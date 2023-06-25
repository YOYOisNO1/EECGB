def program5358():
    n,x,y= map(int,input().split())
    
    print(max(0,n*y/100+1-x) if n*y%100 else n*y/100-x)
     
    
    
    
    
    
    
    