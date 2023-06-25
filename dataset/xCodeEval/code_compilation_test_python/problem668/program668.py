def program668():
    n, k, t=map(int, input().split())
    if(t<k):
        print(t)
    elif(t>k and t<=n):
        print(k)
    elif(t==n+k):
        print(0)
    elif(t>n):
        m=t-n
        print(n-(n+m-k))
        