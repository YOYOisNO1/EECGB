def program3390():
    x=input().split()
    
    d =int(x[0])
    m =int(x[1])
    
    b= max(d,m); s= min(d,m)
    
    while(True):
        if (b%d==0 and b%m==0):
            c=b
            break
        b+=1
    
    y = c/d
    z = c/m
    
    if d>m:
        y+=1
    else:
        z+=1
    
    if y>z:
        print("Dasha")
    
    elif y<z:
        print("Masha")
    
    else:
        print("Equal")