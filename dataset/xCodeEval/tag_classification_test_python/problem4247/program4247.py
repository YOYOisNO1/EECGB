def program4247():
    a,b,c,d=map(int,input().split())
    tri=0
    for j in range(a+b,b+c+1):
        np=(j-a-b)
        if np<=(b-a) and np<=(c-b):
            nways=(np+1)
        if np>(b-a) and np<=(c-b):
            nways=(b-a+1)
        if np<=(b-a) and np>(c-b):
            nways=(c-b+1)
        if np>(b-a) and np>(c-b):
            nways=np+1-(np-(b-a))-(np-(c-b))
            if(np-(b-a+1)-(c-b+1))>0:
                nways=0
            
        if j>c:
            if j<=d:
                tri+=(nways*(j-c))
            else:
                tri+=(nways*(d-c+1))
            
    print(tri)
        