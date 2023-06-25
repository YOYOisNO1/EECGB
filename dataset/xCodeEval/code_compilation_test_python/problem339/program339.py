def program339():
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    a=[(i+j) for i in l[:-1] for j in l[i:-1]]
    i=0
    k=len(a)
    for i in range (k):
        if l[n-1]<a[i]:
            print('YES')
            break
    else:print('NO')
    
        