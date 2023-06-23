    '''
    Created on 12.05.2012
    
    @author: matt
    '''
    
    
def primes(n):
        n = n + 1
        store = [True for i in range(n)]
        store[0] = store[1] = False
        index = 1
        while True:
            index += 1
            while index < n and store[index] == False:
                index += 1
            if index >= n:
                yield n-1
            for i in range(index ** 2, n, index):
                store[i] = False
            yield index
    
def factorize(n):
        MP = int(n // 2 + 1)
        P = primes(MP)
        k = n
        factors = {}
        while k != 1:
            nextp = next(P)
            while k % nextp == 0:
                if not nextp in factors:
                    factors[nextp] = 0
                factors[nextp] += 1
                k //= nextp
        return factors  
        
def solve():
        try: input = input
        except: pass
        N = int(input())
        k = N
        r = N
        factors = factorize(k)
        fs = sorted([(i, j) for i, j in factors.items()])
        for i,j in fs:
            for t in range(j):
                r += k // i
                k //= i
        print str(r)
    
    solve()
        
        