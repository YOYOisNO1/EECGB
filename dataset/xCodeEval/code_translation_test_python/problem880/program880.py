    I = lambda : int(input())
    Is = lambda : map(int,input().split())
    Li = lambda : list(map(int,input().split()))
def solve():
    def is_prime(n):
            i = 2
            while n > i*i and n % i != 0:
                i += 1
            return bool(n<i*i)
        n,m = Is()
        mod = 998244353
        ans = 0
        cur = 1
        div = 1
        for i in range(1,n+1):
            if is_prime(i):
                div *= i
            cur *= m//div
            ans += pow(m,i,mod) - cur % mod
        print(ans%mod)
        return 1
    solve()
    
    	  