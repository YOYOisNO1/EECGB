    import math
def primeFactors(n):
        c=[]
        # Print the number of two's that divide n
        while n % 2 == 0:
            c.append(2)
            n = n // 2
    
        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
        for i in range(3,int(math.sqrt(n))+1,2):
    
            # while i divides n , print(i) ad divide n
            while n % i== 0:
                c.append(i)
                n = n // i
    
        # Condition if n is a prime
        # number greater than 2
        if n > 2:
            c.append(n)
        return c
    n,m = map(int,input().split())
    k = m//n
    l = m%n
    if(l!=0 or (k%3!=0 and k%2!=0)):
        if(n==m):
            print(0)
        else:
            print(-1)
    else:
        z = primeFactors(k)
        if(z.count(2)+z.count(3)==len(z)):
            print(len(z))
        else:
            print(-1)