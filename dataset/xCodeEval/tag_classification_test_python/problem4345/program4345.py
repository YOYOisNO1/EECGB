def program4345():
    n=int(input())
    a=[]
    a=[int(i) for i in input().split()]
    a.sort()
    p = int(a[n-1])
    if p>25:
        print(p-25)
    else:
        print("0")