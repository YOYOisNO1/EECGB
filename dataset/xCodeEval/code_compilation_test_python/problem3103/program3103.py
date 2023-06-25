    import sys
    input = sys.stdin.readline
def main():
      #  t = int(input())
        t = 1
        while(t):
      #  for _ in range(t):
            t -= 1
            
            MOD = 998244353
            fact = [1]*200005
            for i in range(1, 200005):
                fact[i] = i*fact[i-1]
            
        def fast_sq(a, b):
                ans = 1
                if(b == -1):
                    b = MOD-2
                for i in range(60):
                    if((1<<i)&b):
                        ans *= a
                    a *= a
                return ans
            n, m = map(int, input().split())
            print(fact[m]*(n-2)*fast_sq(2, n-3)*fast_sq(fact[n-1]*fact[m-n+1], -1)%MOD)
           
    main()