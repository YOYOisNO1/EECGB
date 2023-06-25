    p = 10**9+7
def power(x, y, p):
        b = bin(y)[2:]
        start = x % p
        answer =1 
        for i in range(len(b)):
            if b[len(b)-1-i]=='1':
                answer = (answer*start) % p
            start = (start*start) % p
        return answer
    
def invert(x, p):
        return power(x, p-2, p)
    
    
def process(n, k):
        a1 = power(2, n*k, p)
        if n % 2==0:
            a2 = (power(2, n-1, p) % p)
            a3 = (a2-1) % p
            R = (invert(2, p)-invert(power(2, n, p), p)) % p
            num1 = (power(R, k+1, p)-R) % p
            den1 = (R-1) % p
            num = (a2*a1*num1) % p
            den = (a3*den1) % p
            entry = (num*invert(den, p)) % p
            return (a1-entry) % p
        else:
            a2 = (power(2, n-1, p)-1) % p
            a3 = (a2+2) % p
            R = (invert(2, p)+invert(power(2, n, p), p)) % p
            num1 = (power(R, k+1, p)-R) % p
            den1 = (R-1) % p
            num = (a2*a1*num1) % p
            den = (a3*den1) % p
            entry = (num*invert(den, p)) % p
            return (a1-entry) % p
        
    t = int(input())
    for i in range(t):
        n,k = [int(x) for x in input().split()]
        print(process(n, k))