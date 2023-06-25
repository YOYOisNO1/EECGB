    """import sys
    input = sys.stdin.buffer.readline
def print(val):
        sys.stdout.write(str(val) + '\n')"""
    
def inverse(n,primemod):
        return pow(n,primemod-2,primemod)
    
def choose(n,k,mod):
        return (factorials[n]*inverses[k]*inverses[n-k])% mod
    
def factorial_creator(n,mod):
        factorials = [1]
        curr = 1
        for i in range(1,n+1):
            curr = (curr*i) % mod
            factorials.append(curr)
        return factorials
    
def inverse_creator(n,k,mod,factorials):
        inverses = []
        for i in range(n-k+1):
            inverses.append(inverse(factorials[i],mod))
        return inverses
    
def place_rooks(n,k,mod):
        if k >= n:
            return 0
        filled = n - k
        placements_per_filled = 0
        for i in range(filled):
            placements_per_filled += (((-1)**i)*choose(filled,i,mod)*pow(filled-i,n,mod)) % mod
            placements_per_filled %= mod
        if k == 0:
            total = (((factorials[n]*inverses[n-k]*inverse(factorials[k],mod))%mod)*placements_per_filled ) % mod
            return total
        total = ((2*(factorials[n]*inverses[n-k]*inverse(factorials[k],mod))%mod)*placements_per_filled ) % mod
        return total
            
    n, k = map(int,input().split())
    factorials = factorial_creator(n,998244353)
    inverses = inverse_creator(n,k,998244353,factorials)
    print(place_rooks(n,k,998244353))