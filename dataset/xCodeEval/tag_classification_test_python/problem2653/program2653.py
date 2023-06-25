def program2653():
    i=input()
    a,b=map(int,i.split())
    
    c=0
    if a%b==0:
        c=a/b
        print(c)
        
    while a%b!=0:
        c+=int(a/b)
        d=b
        b=a%b
        a=d
        if a%b==0 and b!=0:
            c+=a/b
            print(c)