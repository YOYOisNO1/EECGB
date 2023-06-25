    
def solve(n):
        if n == 0:  return 1
        mod = (10 ** 9) + 7
        p = pow(2, n-1, mod)
        return (2 * p + 1) * p % mod
    
def main():
        n = int(input())
        print(solve(n))
    
    main()