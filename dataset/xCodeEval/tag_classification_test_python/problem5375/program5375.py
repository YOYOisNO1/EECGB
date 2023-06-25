    from functools import reduce
    from sys import stdin, gettrace
    
    if gettrace():
    def inputi():
            return input()
    else:
    def input():
            return next(stdin)[:-1]
    
    
    def inputi():
            return stdin.buffer.readline()
    
    MOD = 1000000007
    LIMIT = 200000
    
def solve(n, k):
        if k == 0:
            return 1
        ecomb = pow(2, (n-1), MOD)
        if n%2 == 0:
            e = ecomb -1
            num = (pow(2, k*n, MOD) - pow(e, k, MOD))%MOD
            denom =(pow(2, n, MOD) - e)%MOD
            res = (pow(e, k, MOD) + num*pow(denom, MOD-2, MOD))%MOD
            # res = (pow(e, k, MOD) +
            #        reduce(lambda x, y: (x+y)%MOD,((pow(2, i*n, MOD)*pow(e,k - i -1, MOD)) for i in range(k))))%MOD
            # res = ecomb
            # for i in range(2, k+1):
            #     res = ((ecomb-1)*res + pow(2, (i-1)*n, MOD))%MOD
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