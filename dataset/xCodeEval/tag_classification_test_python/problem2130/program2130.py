def program2130():
    P=1000000007
    A=[1]
    B=[0]
    n,k,d=map(int,input().split())
    for i in range(n):
        S1 = 0
        S2 = 0
        for j in range(k):
            if j<=i:
                S1= (S1+A[i-j])%P
                if (j>=d-1):
                    S2= (S2+A[i-j])%P
                else:
                    S2= (S2+B[i-j])%P
        A.append(S1)
        B.append(S2)
    print((B[n]))
        