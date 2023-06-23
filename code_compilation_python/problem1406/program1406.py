def genprimes(limit):
        lim12 = max(limit, 12)
        lim = lim12 // 6
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
        res = [i for i, s in zip(range(3, lim12, 2), sieve) if s]
        for i, p in enumerate((2, 3, 5, 7)):
            res[i] = p
        return res
    
    
def main():
        from bisect import bisect_left
        n = int(input())
        if n < 9:
            print("1\n" + str(n))
        primes = genprimes(n // 2)
        for a in reversed(primes):
            for b in reversed(primes):
                c = n - a - b
                if primes[bisect_left(primes, c)] == c:
                    print(3)
                    print(a, b, c)
                    return
                if b == a:
                    break
    
    
    if __name__ == '__main__':
        main()