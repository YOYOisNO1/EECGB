    n=int(input())
def somme(x):
        k=0
        ch=str(x)
        if x==0 :
            return 0
        else:
            
            for i in range (len(ch)):
                d=int(ch[i])
                k=k+d
            return k    
    a=0
    b=n
    s1=somme(a)
    s2=somme(b)
    s=s1+s2
    for i in range (1,(n//2)+1,1):
        
        z=somme(a+i)
        y=somme(b-i)
        m=z+y
        if m>s:
            s=m
        
        
    print(s)
        
        