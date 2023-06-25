def program2520():
    n=int(input())
    l=[int(x) for x in input().split()]
    l.sort()
    count=0
    i=0
    while i<n:
        if l[i]!=l[i+1]:
            count+=(l[i+1]-l[i])
        i+=2
    print(count