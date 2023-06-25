    
    MOD = 1000000007
    
def solve(n, k):
        if k == 0:
            return 1
        ecomb = pow(2, (n-1), MOD)
        if n%2 == 0:
            e = ecomb -1
            num = (pow(2, k*n, MOD) - pow(e, k, MOD))%MOD
            denom =(pow(2, n, MOD) - e)%MOD
            res = (pow(e, k, MOD) + num*pow(denom, MOD-2, MOD))%MOD
        else:
            res = pow(ecomb+1, k, MOD)
        return res
    
    
def main():
        t = int(input())
        for _ in range(t):
            n, k = map(int, input().split())
            print(solve(n, k))
    
    
    if __name__ == "__main__":
        main()