    from math import sqrt
    from itertools import combinations
    
    inp=input().split()
    n=int(inp[0])
    k=int(inp[1])
    
    
    
def primeFactors(n): 
        prime_facts=[]
        while n % 2 == 0: 
            prime_facts+=[2] 
            n = n / 2
    
        for i in range(3,int(sqrt(n))+1,2): 
            while n % i== 0: 
                prime_facts+=[i]
                n = n / i 
        if n > 2: 
            prime_facts+=[n]
        return prime_facts
    
    prime_facts=primeFactors(n)
    
    if len(prime_facts)>=k:
        for i in range(k-1):
            print(int(prime_facts[i]),end=" ")
        mult=1
        for i in range(k-1,len(prime_facts)):
            mult*=prime_facts[i]
        print(int(mult),end="")    
    else:
        print(-1)