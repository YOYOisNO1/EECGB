def program1282():
    n,k = map(int,input().split())
    a = (n/2) / (k+1)
    b = k*a
    print(a,b,n-(a+b))