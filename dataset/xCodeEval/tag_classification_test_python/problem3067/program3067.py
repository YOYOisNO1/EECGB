def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    n,a,b,p,q=map(int,input().split())
    m=(a*b)//gcd(a,b)
    if p>q:
        exit(print(((n//a)*p)+((n//b)*q)-(n//m)*q))
    exit(print(((n//b)*q)+((n//a)*p)-(n//m)*p))
    