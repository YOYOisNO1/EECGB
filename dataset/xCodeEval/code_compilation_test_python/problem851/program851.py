def program851():
    n,t=map(int,input().split())
    d=10**(n-1)
    e=10**n
    for i in range(d,e):
        if i%t=0:
            print(i)
            break