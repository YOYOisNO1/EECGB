    from math import sqrt
    
    
def genprimes(limit):
        lim = limit // 6
        sieve = [False, True, True] * lim
        lim = lim * 3 - 1
        for i, s in enumerate(sieve):
            if s:
                p, pp = i * 2 + 3, (i + 3) * i * 2 + 3
                le = (lim - pp) // p + 1
                if le > 0:
                    sieve[pp::p] = [False] * le
                else:
                    break
        sieve[0] = sieve[3] = True
        res = [i * 2 + 3 for i, f in enumerate(sieve) if f]
        for i, p in enumerate((2, 3, 5, 7)):
            res[i] = p
        while res[-1] >= limit:
            del res[-1]
        return res
    
    
def main():
        n, res = int(input()), 1
        if not n % 2:
            res=2
            while not n % 2:
                n //= 2
        for p in genprimes(int(sqrt(n)) + 12):
            if not n % p:
                res *= p
                while not n % p:
                    n //= p
                if n == 1:
                    break
        print(res * n)
    
    
    if __name__ == '__main__':
        main()