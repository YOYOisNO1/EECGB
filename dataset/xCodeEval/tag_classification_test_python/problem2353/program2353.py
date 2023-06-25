def sol(x):
        if x%2==0:
            return 2
        else:
            n=3
            while n*n<=x:
                if x%n==0:
                    return n
                else:
                    n+=2
            return x
    x=int(input())
    
    j=x
    ans=0
    while x%2==1:
        x-=sol(x)
        ans+=1
    print(ans+(x//2))