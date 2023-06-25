def program7273():
    m,n=(float(x) for x in input().split())
    if n==1 and m==1:print(1.0)
    else:
        kart=(m-1)*(n-1)/(n*m-1)
        print((kart+1)/m)