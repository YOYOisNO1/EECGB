    import sys
    from math import gcd
    # sys.setrecursionlimit(10000)
    
    
    class BinaryField:
    def __init__(self, s):
            """Given a binary string, return a BinaryField element.
            Input:
            s: Has to take one of the following form:
               1. A binary string, with MSB as the highest degree polynomial
               2. An integer, with MSB as the highest degree polynomial"""
            if type(s) == int:
                self.poly = s
    
            else:
                self.poly = 0
    
                for c in s:
                    self.poly = (self.poly << 1) + int(c)
    
            if self.poly == 0:
                self.deg = float('-inf')
            else:
                self.deg = len(bin(self.poly)) - 3
    
    def __repr__(self):
            return f'BinaryField(poly={bin(self.poly)[2:]}, deg={self.deg})'
    
    def __eq__(self, other):
            return self.poly == other.poly
    
    def __add__(self, other):
            return BinaryField(self.poly ^ other.poly)
    
    def __mul__(self, other):
            temp = other.poly
            answer = 0
            align = self.poly
    
            while temp:
                if temp & 1:
                    answer ^= align
    
                align <<= 1
                temp >>= 1
    
            return BinaryField(answer)
    
    def __truediv__(self, other):
            if other.poly == 0:
                raise ZeroDivisionError
    
            answer = 0
            temp = self.poly
    
            for d in range(max(self.deg - other.deg, 0), -1, -1):
                if temp & (1 << (other.deg + d)):
                    answer += (1 << d)
                    temp ^= (other.poly << d)
    
            return BinaryField(answer)
    
    def __mod__(self, other):
            if other.poly == 0:
                raise ZeroDivisionError
    
            answer = 0
            temp = self.poly
    
            for d in range(max(self.deg - other.deg, 0), -1, -1):
                if temp & (1 << (other.deg + d)):
                    answer += (1 << d)
                    temp ^= (other.poly << d)
    
            return BinaryField(temp)
    
    def square(self):
            """Returns the square of the polynomial itself.
            Faster than a * a"""
            answer = 0
            temp = self.poly
    
            while temp:
                lsb = temp & (-temp)
                answer += lsb ** 2
    
                temp -= lsb
    
            return BinaryField(answer)
    
    def powmod(self, exp, mod):
            """Return (self**exp) % mod
            Inputs:
            exp: An integer power
            mod: A BinaryField element representing the modulus"""
            answer, temp = BinaryField(1), self
    
            while exp:
                if exp & 1:
                    answer = (answer * temp) % mod
    
                exp >>= 1
                temp = temp.square() % mod
    
            return answer
    
        @staticmethod
    def gcd(poly1, poly2):
            """Given two BinaryField elements, return its gcd
            Input:
            poly1, poly2: two BinaryField elements.
            Output:
            The gcd of poly1 and poly2 as a BinaryField instance."""
            if poly1.deg < poly2.deg:
                poly1, poly2 = poly2, poly1
    
            p1, p2 = poly1, poly2
            while p2.poly != 0:
                p1, p2 = p2, p1 % p2
    
            return p1
    
        @staticmethod
    def factorize(poly):
            """Factorize a BinaryField object
            Input:
            poly: A BinaryField element
            Return: A list of tuples (poly, exp)."""
            answer = []
            temp = poly
    
            for d in range(2, 2**(1+poly.deg//2)):
                div = BinaryField(d)
    
                e = 0
                while temp % div == BinaryField(0):
                    temp = temp / div
                    e += 1
    
                if e:
                    answer.append((div, e))
    
                if temp == BinaryField(1): break
    
            if temp != BinaryField(1):
                answer.append((temp, 1))
    
            return answer
    
    
def input_general():
        return sys.stdin.readline().rstrip('\r\n')
    
    
def input_num():
        return int(sys.stdin.readline().rstrip("\r\n"))
    
    
def input_multi(x=int):
        return map(x, sys.stdin.readline().rstrip("\r\n").split())
    
    
def input_list(x=int):
        return list(input_multi(x))
    
    
def main(s):
    def get_factor(n):
            factors = {1}
    
            for p in range(2, 1 + int(n**0.5)):
                e = 0
    
                while n % p == 0:
                    n //= p
                    e += 1
    
                if e:
                    factors = {f * (p**i) for f in factors for i in range(e+1)}
    
                if n == 1: break
    
            if n != 1:
                factors = {f * g for f in factors for g in (1, n)}
    
            return factors
    
        s = s.rstrip('0')
        leading_0 = s.find('1')
    
        answer = 1
    
        if leading_0 == -1:
            print('-1')
            return
    
        f2s = BinaryField(s)
        x = BinaryField(2)
        factors_bin = BinaryField.factorize(f2s)
    
        for f, exp in factors_bin:
            factors_pow = sorted(list(get_factor(2**f.deg-1)))
    
            for e in factors_pow:
                if x.powmod(e, f) == BinaryField(1):
                    if exp == 1:
                        need = e
                    else:
                        need = e * (2**(len(bin(exp-1)) - 2))
    
                    g = gcd(answer, need)
                    answer = answer * need // g
    
                    break
    
        print(1 + leading_0, 1 + leading_0 + answer)
    
    
    if __name__ == "__main__":
        s = input_general()
    
        main(s)