def program317():
    n=int(input())
    if (n%2==0):
        k=n/2
        d=(n*(n+1))/2
        a=((k*(2+((k-1)*2))))
        print(d-a)
       
    else:
        k=(n+1)/2
        d=(n*(n+1))/2
        a=((k*(2+((k-1)*2))))
        print(d-a)
            