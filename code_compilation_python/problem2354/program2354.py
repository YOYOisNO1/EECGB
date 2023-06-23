def program2354():
    b=int(input())
    M=list(map(int,input().split()))
    s=0
    while M!=[]:
        M.sort()
        B=[0]
        for i in M:
            if i != M[0]:
                if i%M[0]==0:
                    B.append(i)
        B[0]=M[0]
        S=set(M)
        Y=set(B)
        Z=S-Y
        M=list(S)
        s=s+1
    print(s)