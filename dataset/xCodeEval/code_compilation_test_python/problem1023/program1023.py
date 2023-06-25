def program1023():
    nn=input()
    nn=nn.spilt()
    n=int(nn[0])
    m=int(nn[1])
    i=n+1
    while i>0:
        k=0
        for j in range(2,(i//2)+1):
            if i%j==0:
                k=1
                break
        if k==0 and i==m
            print('YES')
            break
        elif k==0 and i!=m
            print('NO')
            break
        i=i+1
        
            