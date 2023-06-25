def program422():
    n=int(input())
    L=sorted([int(i) for i in input().split()])
    print(L[n-1],end=" ")
    for i in range(1,n-1):
        print(L[i],end=" ")
    print(L[0])
        