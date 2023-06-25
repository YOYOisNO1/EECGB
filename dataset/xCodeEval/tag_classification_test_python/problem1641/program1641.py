def program1641():
    import math as m
    a1=int(input())
    a2=int(input())
    k1=int(input())
    k2=int(input())
    yellow=int(input())
    zellow=yellow*1
    mini=9000
    maxi=0
    
    if yellow-((k2*a2)-a2) <= 0 :
        mini=0
    else :
        yellow-=(k2*a2)-a2
        if yellow - ((k1*a1)-a1) <= 0 :
            mini=0
        else :
            yellow-=((k1*a1)-a1)
            rest=a1+a2-yellow
            if rest<=0 :
                mini=a1+a2
            else :
                mini=a1+a2-rest
    yellow=zellow            
    if k1<k2 :
    
        if yellow > k1*a1 :
            maxi+=a1
            yellow-=k1*a1
            if yellow > k2*a2 :
                maxi+=a2
            else :
                rest=k2*a2 - yellow
                rest=m.ceil((rest/k2))
                maxi+=a2-rest
                
                
        else :
            rest=k1*a1 - yellow
            rest=m.ceil((rest/k1))
            maxi=a1-rest
    else :
        if yellow > k2*a2 :
            maxi+=a2
            yellow-=k2*a2
            if yellow > k1*a1 :
                maxi+=a1
            else :
                rest=k1*a1 - yellow
                rest=m.ceil((rest/k1)) 
                maxi+=a1-rest
                
                
        else :
            rest=k2*a2 - yellow
            rest=m.ceil((rest/k2))
            maxi+=a2-rest
    print(mini,maxi)        
                    
            
      
    
            
            
            
            
                
            