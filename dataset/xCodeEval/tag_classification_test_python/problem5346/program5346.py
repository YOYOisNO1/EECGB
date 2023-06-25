    import sys
    import io, os
    import math
    from heapq import *
    gcd = math.gcd
    sqrt = math.sqrt
def ceil(a,b):
        a=-a
        k=a//b
        k=-k
        return k
    # arr=list(map(int, input().split()))
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def strinp(testcases):
        k = 5
        if (testcases == -1 or testcases == 1):
            k = 1
        f = str(input())
        f = f[2:len(f) - k]
        return f
def sieve(n):
        prime = [0 for i in range(n + 1)]
        p = 2
        if (prime[p] == 0):
                for i in range(p * p, n + 1, p):
                    prime[i] = p
        p+=1
        while (p * p <= n):
            if (prime[p] == 0):
                for i in range(p * p, n + 1, p):
                    prime[i] = p
            p += 2
        return prime
def cleanarr(arr):
        n = len(arr)
        #  put comment if arr already sorted
        c = [[arr[0], 1]]
        k = 0
        for i in range(n - 1):
            if (arr[i] != arr[i + 1]):
                c.append([arr[i + 1], 1])
                k += 1
            else:
                c[k][1] += 1
        return c
def factors(l,k):
        if(l==[]):
            return([])
        if(k==len(l)-1):
            ans = [0]*(l[k][1]+1)
            for i in range(l[k][1]+1):
                ans[i]=l[k][0]**i
            return ans
        p=factors(l,k+1)
        og=len(p)
        for i in range(1,l[k][1]+1):
            n=l[k][0]
            for j in range(og):
                p.append(p[j]*(n**i))
        return p
def pfactors(n,l):
        if(l[n]==0):
            return([])
        curr=n
        ans=[]
        while(True):
            f=l[curr]
            if(f==0):
                ans.append(curr)
                break
            ans.append(f)
            curr=curr//f
        ans.sort()
        ans=cleanarr(ans)
        return ans
def main():
        arr=list(map(int, input().split()))
        n=arr[0]
        m=arr[1]
        dp=[0]*(n+2)
        dp[1]=1
        dp[2]=2
        dp[3]=5
        if(n<4):
            print(dp[n])
            sys.exit()
        p=sieve(n)
        for i in range(4,n+1):
            dp[i]=(2*dp[i-1]+1)%m
            f=pfactors(i,p)
            g=factors(f,0)
            for h in range(1,len(g)-1):
                j=g[h]
                f=i//j
                dp[i]+=(dp[i//j]-dp[(i-1)//j])
                dp[i]=dp[i]%m
        print(dp[n])
    main()