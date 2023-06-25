    import math
    
def extended_gcd(aa, bb):
        lastremainder, remainder = abs(aa), abs(bb)
        x, lastx, y, lasty = 0, 1, 1, 0
        while remainder:
            lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
            x, lastx = lastx - quotient*x, x
            y, lasty = lasty - quotient*y, y
        return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
    
def modinv(a, m):
        g, x, y = extended_gcd(a, m)
        if g != 1:
            raise ValueError
        return x % m
    
    n = input()
    fact = [1,1]
    for i in range(2,2000002):
        fact.append(fact[i-1]*i)
        fact[i]%=1000000007
    
    
    print(((2) * fact[2*n+1] * modinv(fact[n],1000000007) * modinv(fact[n+1],1000000007))+1000000006)%1000000007