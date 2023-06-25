    
    #Codeforce 1097D
    
    n,k = map(int, input().split())
    mod =1000000007
    """
def div(a,b):
        if b==1:
            return a%mod
        return (a%mod*(pow(b,mod-2,mod)))%mod
    """
    inv=[0,1]+[pow(b,mod-2,mod) for b in range(2,60)]
    
    dic={}
    
    i=2
    n1=n
    while i*i<=n1:
        while n1%i==0:
            dic[i]=dic.get(i,0)+1
            n1/=i
        i+=1
    if n1!=1:
        dic[n1]=dic.get(n1,0)+1
    
    pdt=1
    for key in dic:
        #print(key,) dic[key]
        m=dic[key]
        ans=[[0]*(m+1) for i in range(k)]
        for idx in range(m+1):
            ans[0][idx]=inv[m+1]
        for i in range(1,k):
            for j in range(m,-1,-1):
                for kxx in range(m,j-1,-1):
                    ans[i][j]=(ans[i][j]+ans[i-1][kxx]*inv[kxx+1])%mod
        #print(ans)
        ax=0
        for i in range(m+1):
            ax=(ax+pow(key,i,mod)*ans[k-1][i])%mod
        pdt=(pdt*ax)%mod
    print(pdt)
    exit()