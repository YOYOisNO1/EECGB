def program872():
    x=int(input())
    x=abs(x)
    n=2
    s=0
    while s!=x:
        s=(pow(n,2)-n)/2
        n=n+1
        if s>x:
            if (s-x)%2==0:
                break
    print(n-2)