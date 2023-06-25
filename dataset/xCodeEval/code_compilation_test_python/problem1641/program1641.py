def f(s,dp):
        if len(s)<=1:
            return 0
        if dp.get(s)!=None:
            return dp[s]
        ans=0
        n=len(s)
        for k in range(n):
            if (k-1>=0 and ord(s[k-1])-ord(s[k])==-1) or  (k+1<len(s) and ord(s[k+1])-ord(s[k])==-1):
                ans=max(ans,1+f(s[:k]+s[k+1:],dp))
        dp[s]=ans
        return ans
    n=int(input())
    s=input()
    dp={}
    print(f(s,dp))