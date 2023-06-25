def program816():
    n=int(input())
    s='ROYGBIV'
    se='GBIV'
    c=n%len(s)
    d=n//len(s)
    f=int((c)%4)
    if(c==0):
        print(s*d)
    else:
        if(c<=4):
            print((s*d)+(se[0:c]))
            
        else:
            if(f==0):
                print((s*d)+(se*(c//4)))
            else:
                print((s*d)+(se*(c//4))+se[0:f])
                
            
        
        
        
        
        
        