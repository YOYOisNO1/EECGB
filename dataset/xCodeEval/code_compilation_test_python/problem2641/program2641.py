def program2641():
    from fractions import gcd
    n,s= int(input()),0
    for i in range(2,n):
        temp=n
        while temp:
            s+=(temp%i)
            temp//=i
    g=gcd(s,n-2)
    print(s//g,end="")
    print("/",end="")
    print(n-2//g)
            from fractions import gcd
    n,s= int(input()),0
    for i in range(2,n):
        temp=n
        while temp:
            s+=(temp%i)
            temp//=i
    g=gcd(s,n-2)
    print(s//g,end="")
    print("/",end="")
    print(n-2//g)
            