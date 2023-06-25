    C=lambda n,k:F[n]*R[k]*R[n-k]%B
def pow(x,y):return 1 if y==0 else (pow(x,y/2)**2)%B if y%2==0 else (pow(x,y-1)*x)%B
    n,w,b=map(int,input().split())
    S,R,F,B,ans=[0]*4445,[1]+[0]*4444,[1]+[0]*4444,1000000009,0
    for i in range(1,4444):F[i],R[i],S[i]=F[i-1]*i%B,pow(F[i-1]*i,B-2)%B,S[i-1]+w-i
    print sum(C(b-1,i-1)*C(w-2,n-2-i)*S[n-i-1] for i in range(1,n))*F[w]*F[b]%B