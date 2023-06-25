def program9():
    n=int(input())
    k=int(input())
    p=0
    l=0
    m=0
    if n==0:
        print('Impossible')
    else:
        if n>=k:
            m=n-k
            print(m+n)
        else:
            m=k-n
            print(m+n)
        l=n+k-1
        print(l)