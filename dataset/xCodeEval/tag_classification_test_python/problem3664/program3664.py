    import random as r 
def isprime(n):
        k=5
        if n<=1 or n==4:
            return 0 
        if n<=3:
            return 1 
        while k:
            a=2+r.randint(1,n-4)
            if pow(a,n-1,n)!=1: return 0 
            k-=1 
        return 1 
    for _ in range(int(input())):
        a,b=map(int,input().split())
        print('YES' if isprime(a*a-b*b) else 'NO')