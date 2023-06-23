def cmb(n, r, mod):#コンビネーションの高速計算　
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod
    
    mod = 998244353 #出力の制限
    N = 5*10**5+1
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル
    
    for i in range( 2, N + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append( (g2[-1] * inverse[-1]) % mod )
    
    n,k=map(int,input().split())
    ans=0
    for i in range(1,n+1):
        count=n//i-1
        if count>=k-1:
            ans+=cmb(count,k-1,mod)
        ans%=mod
    
    print(ans%mod)