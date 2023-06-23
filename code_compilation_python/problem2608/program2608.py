def program2608():
    a,b = map(int,input().split())
    w1,h1 = map(int,input().split())
    w2,h2 = map(int,input().split())
    a+=(b+1)*b/2-(h1+1)*h1/2+h1
    a = max(a-w1,0)
    a+=(h1+1)*h1/2-(h2+1)*h2/2+h2
    a = max(a-w2,0)
    a+=(h2+1)*h2/
    print(a)