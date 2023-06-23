    
    n=int(input())
    
def ct(n):
        s=[0]
        for i in range(1,n+1):
            sx=[]
            for k in s:
                for m in [1,5,10,50]:
                    if k+m not in sx:
                        sx.append(k+m)
            s=sx
        return len(s)
    
    
    if n<=12:
        print ct(n)
        exit()
    
    print (n-12)*49
    exit()
    
    
    
    
    
    
    
    