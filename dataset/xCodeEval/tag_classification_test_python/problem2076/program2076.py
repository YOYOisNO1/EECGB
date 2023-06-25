def program2076():
    n,k,d=map(int,input().split())
    dp =[1]+ [0]*(n)
    for j in range(1,n+1):
        for i in range(1,k+1):
            p=j-i
            if p>=0:
                dp[j]+=dp[p]
            else:
                break
    dp1=[1]+[0]*n
    for j in range(1,n+1):
        for i in range(1,d):
            if i!=d:
                p=j-i
                if p>=0:
                    dp1[j]+=dp1[p]
                else:
                    break
    mod = 1000000007
    print((dp[n]-dp1[n])%(mod))