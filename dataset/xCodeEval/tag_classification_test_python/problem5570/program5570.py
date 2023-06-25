def program5570():
    x,nn = map(int, input().split())
    n=x
    s=[]
    if n%2 ==0:
        s.append(2)
    while n%2==0:
        n=n//2
    import math
    i=3
    while i<= int(math.sqrt(n)):
        if n%i==0:
            s.append(i)
        while n%i==0:
            n=n//i
        i+=1
    if n>1:
        s.append(n)
    
    # su=0
    ans=1
    for i in s:
        k=i
        su=0
        while k<=nn:
            su=nn//k
            k*=i
            ans*=pow(i,su,1000000007)
            ans%= 1000000007
        # ans*i
    print(ans)