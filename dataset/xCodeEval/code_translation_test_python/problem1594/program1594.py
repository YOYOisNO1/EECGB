    primes = []
    for p in range(2, 6000):
        is_prime = True
        for p2 in primes:
            if p2*p2 > p:
                break
            if p % p2==0:
                is_prime = False
                break
        if is_prime:
            primes.append(p)
            
def factor(n):
        d = {}
        for p in primes:
            if p*p > n:
                break
            if n % p==0:
                c = 0
                while n % p==0:
                    n = n//p
                    c+=1
                d[p] = c
        if n > 1:
            d[n] = 1
        return d
    
def factors(n):
        d = factor(n)
        answer = [1]
        for p in d:
            a2 = []
            for x in answer:
                for i in range(d[p]+1):
                    a2.append(x*p**i)
            answer = a2
        return answer
            
    
def process(n, m):
        f_dict = {0: 0, 1: 1, 2: 2}
        for i in range(3, n+1):
            f_dict[i] = 2*f_dict[i-1]
            for x in factors(i):
                if 2 <= x <= i:
                    f_dict[i] += f_dict[(i//x)]-f_dict[(i-1)//x]
                    f_dict[i] = f_dict[i] % m
            f_dict[i] = f_dict[i] % m
        return f_dict[n]
    
    n, m = [int(x) for x in input().split()]
    print(process(n, m))