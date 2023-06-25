def program1655():
    n=int(input())
    a=[int(i) for i in input().split()]
    k=0
    while a[0]<=max(a[1:]):
        a[1+a[1:].index(max(a))]-=1
        a[0]+=1
        k+=1
    print(k)