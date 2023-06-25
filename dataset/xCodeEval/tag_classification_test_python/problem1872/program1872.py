def program1872():
    n=int(input())
    r=0
    a=list(map(int,input().split()))
    for i in range(n):
        r+=i*4*a[i]
    print(r)