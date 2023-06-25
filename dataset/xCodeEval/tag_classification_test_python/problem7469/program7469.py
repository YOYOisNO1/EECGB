    ans = 0
    mod = 1000000007
    f = [1]*17
    for i in xrange(1, 17):
        f[i] = (i*f[i-1])%mod
def dfs(Id, bNum, cSum, n):
        global ans
        if Id == n:
            ans += 1
            if ans >= mod : ans -= mod
            return 0    
        for i in xrange(n):
            if bNum&(1<<i): continue
            if cSum&(1<<( (Id+i)%n ) ): continue
            dfs(Id+1, bNum|(1<<i), cSum|(1<<( (Id+i)%n ) ), n )
    num = [1, 18, 1800,670320,734832000,890786230,695720788,150347555]
    if __name__ == '__main__':
        ans = 0
        n = input()
        if not n&1:
            print('0')
        else :
            #dfs(0, 0, 0, n)
            #print(ans*f[n]%mod)
            print(num[n>>1])
        
        