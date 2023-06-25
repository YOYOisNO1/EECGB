def program913():
    m,n=[int(x) for x in inpit()split()]
    if m>1 and n>1:
        a=(m//2)*n 
        b=(m%2)*(n//2)
        print(a+b)
    else:
        if m==1 and n==1:
            print(0)
        else:
            print(1)