def program2541():
    n=int(input());
    k=1;
    p=6;
    n-=1;
    for i in range (n):
        k*=2;
        p=p*(4**k)
        p%=1000000007
    
    print((int)p);