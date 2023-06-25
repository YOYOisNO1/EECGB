def program3355():
    p, y = map(int,input().split())
    a = list()
    for i in range(2,p+1):
        for j in range(1,(y//2)+1):
            if(i*j<=y):
              a.append(i*j)
    
    #print(a)
    b = list()
    for i in range(2,y+1):
        b.append(i)
    #print(b)
    z = list(set(b)-set(a))
    z.sort(reverse=True)
    if(len(z)>0):
        print(z[0])
    else:
        print(-1)