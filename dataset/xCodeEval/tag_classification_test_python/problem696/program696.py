def program696():
    n,m=list(map(int,input().split()))
    i=0
    while(m>i):
        m=m-i-1
        i=(i+1)%n
    print(m)