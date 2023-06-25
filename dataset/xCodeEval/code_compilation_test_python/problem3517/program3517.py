def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b,a%b)
    n,m,z = map(int,input().split())
    if m == 0:
        print(0)
    elif (n==m):
        print(z//n)
    else:
        print(z//(gcd(n,m))