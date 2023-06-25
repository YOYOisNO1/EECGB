def program2306():
    from fractions import gcd
    x=input()
    n=x/2
    m=x-n
    while gcd(n,m)!=1:
        m+=1
        n-=1
    print(n,m)