def multiple(i):
        j = i 
        while j <= n:
            yield j
            j += i
def find_factor(n):
        divisor = []
        for i in range(1,int(n**(1/2))+1):
            if n%i == 0:
                divisor.append(i)
                divisor.append(n//i)
        return set(divisor)
    count = 0
    n = int(input())
    prime = [i for i in range(2,n+1)]
    true_prime = []
    while len(prime) > 0:
        # print(prime[0])
        true_prime.append(prime[0])
        cross = [a for a in multiple(prime[0])]
        prime = [i for i in prime if i not in cross]
        
    prime = [i for i in range(2,n+1)]
    for n in prime:
        factor = find_factor(n)
        count = count + 1 if len([i for i in factor if i in true_prime]) == 2 else count
    
    print(count)
        