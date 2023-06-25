    import sys
    
    input = sys.stdin.readline
    
    
def solve():
        n, k = map(int, input().split())
        m = 10**9 + 7
        val = pow(2, n-1, m)
        if n % 2:
            val += 1
            val %= m
            return pow(val, k, m)
        else:
            R = pow(val+1, m-2, m)
            ans = ((pow(2, n*k, m) - pow(val-1, k, m)) % m * R % m)
            ans += pow(val-1, k, m)
            ans %= m
            return ans
    
    
    for _ in range(int(input())):
        print(solve())