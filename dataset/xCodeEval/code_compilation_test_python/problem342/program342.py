def program342():
    s=input()
    n=len(s)
    
    if n%2 == 0:
     
        x = int((n/2)-1)
        y = int(n/2)
        while x>=0:
        
            print(s[x]+s[y],end="")
            x=x-1
            y=y+1
        
    
    else:
    
        
        print(s[int(n/2)],end="")
        x=int((n/2)+1)
        y=int((n/2)-1)
        while y>=0:
        
            print(s[x]+s[y],end="")
            x=x+1
            y=y-1