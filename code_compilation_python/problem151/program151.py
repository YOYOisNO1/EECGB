    #! /usr/bin/env python
    import sys
    
def big_powers(primes, n):
        result = []
        for p in primes:
            p_in_deg = p**3
            while p_in_deg <= n:
                result.append(p_in_deg)
                p_in_deg *= p
        return set(result)
    
def make_power_primes(primes, n):
        result = []
        for p in primes:
            p_in_deg = p
            while p_in_deg <= n/2:
                result.append(p_in_deg)
                p_in_deg *= p
        return set(result)
    
def make_primes(n):
        result = [2]
        for i in range(3,n+1):
            add = True
            for x in result:
                if (i % x == 0):
                    add = False
            if add:
                result.append(i)
        return result
                
    
def main():
        n = int(sys.argv[1])
        #print n
        primes = make_primes(n/2)
        #print "primes = " , primes
        power_primes = make_power_primes(primes, n)
        #print "power_primes = ", power_primes
        almost_almost_primes = set([x*y for x in power_primes for y in power_primes if x*y <= n and x<>y])
        #print "almost_almost_primes = ", almost_almost_primes
        #print "big_powers_prime = ", big_powers(primes, n)
        print len([x for x in almost_almost_primes if not (x in big_powers(primes, n))])
        
        
    
    if __name__ == "__main__":
        main()