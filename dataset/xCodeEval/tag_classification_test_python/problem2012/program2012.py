def program2012():
    n,k,d=map(int,input().split())
    
    s1=[0]*110
    s2=[0]*110
    s1[0],s2[0]=1,1
    mod = 10**9+7
    
    for i in range(1,n+1):
        for j in range(1,k+1):
            if(j>i):
                break
            else:
                s1[i]+=s1[i-j]
        # print(s1[i])
    
        for j in range(1,d):
            if(j>i):
                break
            else:
                s2[i]+=s2[i-j]
    print((s1[n]-s2[n])%mod)
    