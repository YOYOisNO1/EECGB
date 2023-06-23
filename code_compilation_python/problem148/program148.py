    #!/usr/bin/python
    import sys
    import math
    import fractions
    
def sieve(n):
        A = [True for i in range(n + 1)]
        for i in range(2, int(math.sqrt(n)) + 1):
            if A[i]:
                for j in range(i * i, n + 1, i):
                    A[j] = False
        res = []
        for i in range(2, n + 1): 
            if A[i]: res.append(i)
        return res
    
def factor(n):
        base = sieve(n / 2)
        """
        i = len(base) - 1
        fact = {}
        while n > 1 and i >= 0:
            if n % base[i] == 0:
                n /= base[i]
                if base[i] in fact: fact[base[i]] += 1
                else: fact[base[i]] = 1
            else:
                i -= 1
        """
        
        start = int(math.sqrt(n))
        pairs = []
        factors = set([1, n])
        for i in range(start,n):
            for j in range(len(base)):
                lhs = i ** 2 % n
                rhs = base[j] ** 2 % n
                if lhs == rhs: 
                    pairs.append([i,base[j]]);
        for i in range(len(pairs)):
            factors |= set([fractions.gcd(pairs[i][0]-pairs[i][1],n)])
        res = list(factors)
        res.sort()
        return res
        
    
def mod_equation(a, b):
        if a < b: return 0
        if a == b: return 'infinity'
        if a - b == 1:
            if a == 1: return 1
            else: return 0
        #fact = factor(a - b)
        c = a - b
        res = 0
        for i in range(b + 1, (a + b) / 2 + 1):
            if c % i == 0: res += 1
        if a > 1: res += 1
        return res
        
        """
        i = 0
        j = len(fact) - 1
        while j - i > 1:
            mid = (i + j) / 2
            if fact[mid] > b: j = mid
            else: i = mid
        return len(fact) - j
        """
        
    if __name__ == '__main__':
        
        num = sys.stdin.readline().split()
        a = int(num[0])
        b = int(num[1])
        print mod_equation(a, b)
        
        #print factor(9435152-272)