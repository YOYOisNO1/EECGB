    n,k,d=list(map(int,input().split()))
    dict1={}
    for i in range(1,n+1):
        str1=str(i)+"_"+"1"+"_"+"1"
        dict1[str1]=i
    for i in range(1,k+1):
        str1="1"+"_"+str(i)+"_"+"1"
        dict1[str1]=1
def solve(n,k,d,z):
        str1=str(n)+"_"+str(k)+"_"+str(d)
        if n==0 or n==d:
            return 1
        if d>k or n<0 or d>n:
            return 0
        if str1 in dict1.keys():
            return dict1[str1]
        else:
            ans=0
            for i in range(k,d-1,-1):
                ans+=solve(n-i,k,1,z)
                ans%=z
            for j in range(1,d):
                ans+=solve(n-j,k,d,z)
                ans%=z
            dict1[str1]=ans
            return ans
    z=(10**9)+7
    print(solve(n,k,d,z))