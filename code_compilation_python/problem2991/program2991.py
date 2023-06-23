def program2991():
    a,b,c,n=[int(x) for x in input().split()]
    l=a+b-c
    if a<c or b<c:
        print(-1)
    else if l<n:
        print(n-l)
    else:
        print(-1)