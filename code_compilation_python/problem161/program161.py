def program161():
    t=int(input())
    for i in range(t):
        n=int(input())
        k=int(input())
        d=int(input())
        a=list(range(n))
        l=[[] for q in range(n-d+1)]
        for j in range (n):
            a[j]=int(input())
        for p in range (n-d+1):
            for j in range(1, d+1):
                if l[p].count(a[p-1+j])==0:
                    l[p].append(a[p-1+j])
        for p in range (n-d+1):
            l[p]=len(l[p])
        print(min(l))