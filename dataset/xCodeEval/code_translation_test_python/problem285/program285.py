def program285():
    N = 1000000000000
    N_SQRT = 1000000
    
    if __name__ == '__main__':
        is_prime = [True] * (N_SQRT + 1)
        prime = []
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, N_SQRT + 1):
            if is_prime[i]:
                prime.append(i)
                for j in range(i + i, N_SQRT + 1, i):
                    is_prime[j] = False
        n = int(input())
        prime_factors = []
        for i in prime:
            if n % i == 0:
                prime_factors.append(i)
                while n % i == 0:
                    n = n // i
        if n != 1:
            prime_factors.append(n)
        if len(prime_factors) == 0:
            print(n)
        elif len(prime_factors) == 1:
            print(prime_factors[0])
        else:
            print(1)