    
    MOD = 998244353
    choose=[[0 for _ in range(300)] for __ in range(300)] # alternative pre-calculation of nCr
    choose[1][0]=choose[1][1]=1
    for n in range(1,300): # pascal's triangle
        for r in range(n+1):
            if r-1>=0:
                choose[n][r]+=choose[n-1][r-1]
            choose[n][r]+=choose[n-1][r]
            choose[n][r]%=MOD
    
def main():
        
        n, k = readIntArr()
        n -= 1  # ignore root
        dp = [[0 for _ in range(k + 1)] for __ in range(n)]
        # dp[i][j] is number of ways at for first items until index i, with max value at j
        dpprefixsums = [[0 for _ in range(k + 1)] for __ in range(n)]
        # dpprefixsums[i][j] = dp[i][1] + dp[i][2] + ... dp[i][j]
        for j in range(1, k + 1):
            dp[0][j] = 1
            dpprefixsums[0][j] = 1 + dpprefixsums[0][j - 1]
        
        for i in range(1, n):
            for j in range(1, k + 1):
                total = 0
                for max_cnts in range(1, i + 2):
                    if max_cnts == i + 1:  # all j
                        edgecnts = choose[i + 1][2]  # will not exceed MOD
                        total += pow(k - j + 1, edgecnts, MOD)
                        total %= MOD
                    else:
                        firstcomponent = 0
                        ii = i - max_cnts
                        # for jj in range(1, j):
                        #     firstcomponent += dp[ii][jj]
                        #     firstcomponent %= MOD
                        firstcomponent = dpprefixsums[ii][j - 1]
                        chg = firstcomponent
                        chg *= choose[i + 1][max_cnts]  # choose max_cnts (edge == j) among all i
                        chg %= MOD
                        
                        # account of edges from max nodes to other nodes
                        edgecnts = max_cnts * (i + 1 - max_cnts)
                        if max_cnts >= 2:
                            edgecnts += choose[max_cnts][2]
                        chg *= pow(k - j + 1, edgecnts, MOD)
                        chg %= MOD
                        total += chg
                        total %= MOD
                        
                        
                dp[i][j] = total
                dpprefixsums[i][j] = (total + dpprefixsums[i][j - 1]) % MOD
        
        ans = 0
        for j in range(k + 1):
            ans = (ans + dp[n - 1][j]) % MOD
        print(ans)
        
        return
    
    import sys
    input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
    # input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.
     
def oneLineArrayPrint(arr):
        print(' '.join([str(x) for x in arr]))
def multiLineArrayPrint(arr):
        print('\n'.join([str(x) for x in arr]))
def multiLineArrayOfArraysPrint(arr):
        print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))
     
def readIntArr():
        return [int(x) for x in input().split()]
# def readFloatArr():
    #     return [float(x) for x in input().split()]
     
def makeArr(defaultValFactory,dimensionArr): # eg. makeArr(lambda:0,[n,m])
        dv=defaultValFactory;da=dimensionArr
        if len(da)==1:return [dv() for _ in range(da[0])]
        else:return [makeArr(dv,da[1:]) for _ in range(da[0])]
     
def queryInteractive(a, b, c):
        print('? {} {} {}'.format(a, b, c))
        sys.stdout.flush()
        return int(input())
     
def answerInteractive(x1, x2):
        print('! {} {}'.format(x1, x2))
        sys.stdout.flush()
     
    inf=float('inf')
    # MOD=10**9+7
    # MOD=998244353
     
    from math import gcd,floor,ceil
    import math
    # from math import floor,ceil # for Python2
     
    for _abc in range(1):
        main()