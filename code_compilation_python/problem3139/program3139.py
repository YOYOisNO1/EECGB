def program3139():
    import math
    x=int(input())
    ans=10**18
    for i in range(1,int(x**.5)+1):
        if x%i==0:
            if (math.gcd(i,x//i)==1:
                if max(i,x//i)<ans:
                    ans=max(i,x//i)
                    a=[i,x//i]
    print(*a)