    import sys
    input = lambda : sys.stdin.readline().rstrip()
    
    sys.setrecursionlimit(2*10**5+10)
    write = lambda x: sys.stdout.write(x+"\n")
    debug = lambda x: sys.stderr.write(x+"\n")
    writef = lambda x: print("{:.12f}".format(x))
    
    
    ### 素数の逆元とCombination
    
    M = 10**9+7 # 出力の制限
    # M = 998244353
    N = 2*10**5+10 # 必要なテーブルサイズ
    g1 = [0] * (N+1) # 元テーブル
    g2 = [0] * (N+1) #逆元テーブル
    inverse = [0] * (N+1) #逆元テーブル計算用テーブル
    g1[0] = g1[1] = g2[0] = g2[1] = 1
    inverse[0], inverse[1] = [0, 1] 
    for i in range( 2, N + 1 ):
        g1[i] = ( g1[i-1] * i ) % M 
        inverse[i] = ( -inverse[M % i] * (M//i) ) % M # ai+b==0 mod M <=> i==-b*a^(-1) <=> i^(-1)==-b^(-1)*aより
        g2[i] = (g2[i-1] * inverse[i]) % M 
def cmb(n, r, M=M):
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return ((g1[n] * g2[r] % M) * g2[n-r]) % M
def perm(n, r, M=M):
        if (r<0 or r>n):
            return 0
        return (g1[n] * g2[n-r]) % M
def sub(n,k):
        ans = 0
        for v in range(1<<k):
            for v2 in range(1<<k):
                if v&v2>=v^v2:
                    ans += 1
        return ans
def sub3(n,k):
        ans = 0
        for v in range(1<<k):
            for v2 in range(1<<k):
                for v3 in range(1<<k):
                    if v&v2&v3>=v^v2^v3:
                        ans += 1
        return ans
    
def sub2(n,k):
        val = 0
        for i in range(0,n+1,2):
            val += cmb(n,i)
            if val>M:
                val -= M
        if k==0:
            ans = 1
        else:
            if n%2==1:
                ans = pow(1+val, k, M)
            else:
                ans = 0
                v = 1
                v2 = pow(2, n*(k-1), M)
                inv = pow(pow(2, n, M), M-2, M)
                for i in range(k):
                    ans += v * v2 % M
                    v *= (val-1)
                    v%= M
                    v2 *= inv
                    v2 %= M
                    if ans>M:
                        ans -= M
                ans += pow(val-1, k, M)
        return ans
    t = int(input())
    res = []
    for _ in range(t):
        n,k = list(map(int, input().split()))
        ans = sub2(n,k)
        res.append(ans%M)
    #     print(val)
    write("\n".join(map(str, res)))