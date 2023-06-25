    import math
    
    class Rational : 
        
    def __init__ (self, a, b) :
            a, b = int(a), int(b)
            g = math.gcd(a, b)
            self.a = a / g
            self.b = b / g
    
    def __mul__ (self, t) :
            return Rational(self.a * t.a, self.b * t.b)
    
    def __add__ (self, t) : 
            a = self.a * t.b + self.b * t.a
            b = self.b * t.b
            return Rational(a, b) 
    
    def __sub__ (self, t) : 
            a = self.a * t.b - self.b * t.a
            b = self.b * t.b
            return Rational(a, b) 
            
    def __le__ (self, t) : 
            return self.a * t.b <= self.b * t.a
    
    def __repr__ (self) :
            return f'{self.a / self.b}' 
    
def nC3 (n) :
        if n >= 3 : 
            return (n * (n - 1) * (n - 2)) // 6
        return 0
    
def nC2 (n) :
        if n >= 2 : 
            return (n * (n - 1)) // 2
        return 0
    
    stuff = input().split()
    n, p = stuff
    n = int(n)
    p = float(p) 
    p = Rational(1e9 * p, 1e9)
    
    one = Rational(1, 1)
    nc3 = nC3(n)
    
    for k in range(0, n + 1) : 
        t = Rational(nC3(k), nc3)
        t = t + (Rational(1, 2) * Rational(k * nC2(n - k), nc3)) 
        t = t + Rational((n - k) * nC2(k), nc3)
        if p <= t: 
            break
    print(k)