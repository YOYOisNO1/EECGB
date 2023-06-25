def program731():
    a,b=map(int,input().split())
    p=0
    ans=0
    x1=0
    y1=0
    z1=0
    
    x2=0
    y2=0
    z2=0
    while a%2==0:
        x1+=1
        a=a//2
    while a%3==0:
        y1+=1
        a=a//3
    while a%5==0:
        z1+=1
        a=a//5
        
    f1=a
    
    while b%2==0:
        x2+=1
        b=b//2
        
    while b%3==0:
        y2+=1
        b=b//3
    while b%5==0:
        z2+=1
        b=b//5
        
    f2=b
    if f1!=f2:
        print(-1)
    else:
        print(abs(x1-x2)+abs(y1-y2)+abs(z1-z2))
    
            