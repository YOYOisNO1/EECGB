    
def p3(a,b):
        
        while a!=0 and b!=0:
            
        if(a>=2*b):
            a%=(2*b)
            return p3(a,b)
        if(b>=2*a):
            b%=(2*a)
            return p3(a,b)
        return(a,b)
    
    a,b=input().split(" ")
    a,b=p3(int(a),int(b))
    
    print(a,b)