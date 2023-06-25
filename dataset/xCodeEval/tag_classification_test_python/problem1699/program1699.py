def program1699():
    import math
    for _ in range(int(input())):
        n=int(input())
        m=100-n
        k=math.gcd(m,n)
        m=m//k;
        n=n//k;
        print(m+n)