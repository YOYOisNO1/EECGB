    import math
    n=int(input())
    p=[0 for _ in range(1001)]
    x=2
    p[0]=1
    p[1]=1
    while x*x<=1001:
        for i in range(2*x,1001,x):
    
            p[i]=1
        x+=1
    pr=0
def isprime(num):
        for i in range(2,int(math.sqrt(n))+1):
            if num%i==0:
                return False
        return True
    e=0
    if isprime(n):
        print(1)
        print(n)
        exit(0)
    for k in range(n,1,-1):
        if isprime(k):
            if (n-k)%2==0:
             pr=n-k
             e=1
             break
           
    if pr==2:
        print(2)
        print(2,n-2)
        exit(0)
    
    for i in range(2,1001):
        if p[pr-i]==0 and p[i]==0:
            print(3)
            print(n-pr,i,pr-i)
            exit(0)
    
    
     