    import sys
    
    input = sys.stdin.readline
    
    
def ri(): return [int(i) for i in input().split()]
    
    
def rs(): return input().split()[0]
    
    
def main():
        t = 1
    
        for _ in range(t):
            n, m = ri()
            ans = [0] * (n + 1)
            sum = [0] * (n + 2)  # ans[x] + ... + ans[n]
            ans[n] = 1
            sum[n] = 1
            for x in range(n - 1, 0, -1):
                extra = sum[x + 1]  # jump by subtraction
    
                # jump by division
                for d in range(2, n // x + 1):
                    from_ = x * d
                    to_ = min(x * d + d - 1, n)
                    extra = (extra + m + sum[from_] - sum[to_ + 1]) % m
    
                ans[x] = extra
                sum[x] = (sum[x + 1] + ans[x]) % m
            # print(ans)
            print(ans[1] % m)
    
    
    main()