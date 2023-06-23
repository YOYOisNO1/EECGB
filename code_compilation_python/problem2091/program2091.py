def program2091():
    n=int(input())
    a=input().split()
    a=[int(a[i]) for i in range(n)]
    a=sorted(a,None,None,True)
    a[1:n-1]=sorted(a[1:n-1])
    for i in range(n) :
    print(a[i])