    import sys
    import collections
    
    infile = sys.stdin.buffer
def gs()  : return infile.readline().rstrip()
def gi()  : return int(gs())
def gss() : return gs().split()
def gis() : return [int(x) for x in gss()]
    
    MOD = (10 ** 9) + 7
    INF = 10 ** 10
    
def pow(a,n):
        if n == 0: return 1
        t = pow(a,n//2)
        ans = (t * t) % MOD 
        return ans * (a if n &1 else 1) % MOD
    
def compute(n):
        if n & 1:
            return pow(2, n-1)
        return pow(2, n-1) -1
    
    
    
def dfs(i, k, n,s,mem):
        if i == k:
            return 1
        prev = 1
        p = pow(2,n)
        c = 1
        for i in range(k-1,-1,-1):
            ans = 0
            ans += c
            c*= p
            c %= MOD
            if ans > MOD: ans -= MOD    
            ans += (s * prev) %MOD
            if ans > MOD: ans -= MOD
            prev = ans
        return ans
    
    
def f(n,k):
    
        s = compute(n)
        
        if n & 1:
            return pow(1 + pow(2,n-1),k)
    
        #mem = [-1 for ii in range(k+1)]
        #for i in range(k, -1, -1):dfs(i, k, n, s, mem)
        return dfs(0 , k, n,s,[])
    
def main(infn="") :
        global infile
        infile = open(infn,"r") if infn else open(sys.argv[1],"r") if len(sys.argv) > 1 else sys.stdin
        
        ######################################################################
        cn = int(input())
        for u in range(cn):
            n,k = map(int, input().split())
            print((f(n,k)))
        ######################################################################
    
    if __name__ == '__main__' :
        main()
        #sys.stdout.flush()