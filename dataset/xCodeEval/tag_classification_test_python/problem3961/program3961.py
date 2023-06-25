def program3961():
    n,m=map(int,input().split())
    for k in range(33):
        m=min(m,abs(n**(32-k)-m))
    print(["NO","YES"][m==0])