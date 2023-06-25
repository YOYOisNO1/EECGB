def program475():
    ch = input ()
    l=[]
    for i in range (10):
        l.append(input())
    s=""
    res=""
    for i in ch :
        s+=i
        if (len(s)==10):
            a=l.index(s)
            
            res+=str(a)
            s=""
    
        
    print((res))