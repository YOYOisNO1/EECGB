def readline():
        return map(int, input().split())
    
    
def gcd(a, b): return a if b == 0 else gcd(b, a % b)
    
    
def is_prime(p):
        for i in range(2, p):
            if i * i > p: break
            if p % i == 0: return False
    
        return True
    
    
def divisors(n):
        p = 2
        while n > 1 and p * p <= n:
            if n % p == 0: yield p
            while n % p == 0: n /= p
            p += 1
        if n > 1: yield n
    
    
def main():
        a, b = readline()
        g = gcd(a, b)
        a /= g
        b /= g
        
        answer = 0
        
        while b > 0:
            arr = map(lambda p: b // p * p, divisors(a))
            if len(arr) != 0:
                new_b = max(arr)
            else:
                new_b = 0
    
            answer += b - new_b
    
            b = new_b
            g = gcd(a, b)
            a /= g
            b /= g
    
        print answer
    
    
    if __name__ == '__main__':
        main()