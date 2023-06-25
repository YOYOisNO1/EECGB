def program1529():
    r,h=map(float,input().split())
    if h < r/2:
        print(1)
        exit()
    h-=r/2
    R=2
    c=int(h/r)
    
    R+=2*c
    
    h-=c*r
    if ((r/2 + h)**2 + (r/2)**2)**0.5 >= r:
        R +=1
    print(R)