def program4851():
    a,b=map(int, input().split())
    m=1000000007
    B = int((b*(b-1)/2) % m );
    A1 = int((a*(a+1)/2) % m );
    A = int((A1*b+a) % m );
    res = int((A*B) % m) ;
    print(res)