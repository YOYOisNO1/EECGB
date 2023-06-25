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
def main():
        arr=list(map(int, input().split()))
        n=arr[0]
        m=arr[1]
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        dp[3]=5
        if(n<4):
            print(dp[n])
            sys.exit()
        for i in range(4,n+1):
            dp[i]=(2*dp[i-1]+1)%m
            p=int(i**(0.5))
            for j in range(2,p+1):
                if(i%j==0):
                    if(j*j==i):
                        dp[i]+=(dp[i//j]-dp[(i-1)//j])
                        dp[i]=dp[i]%m
                    else:
                        f=i//j
                        dp[i]+=(dp[i//j]-dp[(i-1)//j])
                        dp[i] += (dp[i // f] - dp[(i - 1) // f])
                        dp[i]=dp[i]%m
        print(dp[n])
    main()