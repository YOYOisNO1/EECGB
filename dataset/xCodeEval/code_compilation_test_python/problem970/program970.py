def program970():
    a,b,c,d=map(int,input().split())
    l=[]
    for i in range(a,b+1):
        for j in range(b,c+1):
            for k in range(c,d+1):
                l.append((i+j,k))
    c=0
    for i in range(len(l)):
        if(l[i][0]>l[i][1]):
            c+=1
    print(c)