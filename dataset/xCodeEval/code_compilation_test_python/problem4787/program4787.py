    import sys
    import collections
    
    infile = sys.stdin.buffer
def gs()  : return infile.readline().rstrip()
def gi()  : return int(gs())
def gss() : return gs().split()
def gis() : return [int(x) for x in gss()]
    
    MOD = 10 ** 9 + 7
    INF = 10 ** 12
    N = 10 ** 5
    
    
    
def main(infn="") :
        global infile
        infile = open(infn,"r") if infn else open(sys.argv[1],"r") if len(sys.argv) > 1 else sys.stdin
        ######################################################################
        n,m = gis()
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        h = [0 for _ in range(n+1)]
        cumul = 0
        prev = dp[1]
        h[2]-=1
        for u in range(1, len(dp)):
            if u > 1:
                dp[u] += prev + dp[1]
                dp[u] %= m
    
                cumul += h[u]
                cumul %= m
                
                dp[u] += cumul
                dp[u] %= m
                
                prev += dp[u]
                prev %= m
            '''u = 7
            14 + 0, 14 + 1, 14 + 2
            7        7         8
            '''
            j = 2
            while( j * u < len(dp)):
                h[j*u] += dp[u]
                h[j*u] %= m
                if j*u + j< len(dp):
                    h[j*u + j] -= dp[u]
                    h[j*u + j] %= m
                j+=1
        print (dp[-1])
    
        ######################################################################
    if __name__ == '__main__' :
        main()