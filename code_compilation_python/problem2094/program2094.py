def program2094():
    from itertools import permutations as pr
    n=int(input())
    a=list(map(int,input().split()))
    s=sum((x-y) for x,y in zip(a,a[1:]))
    # print(max(sum(abs(x-y) for x,y in zip(b,b[1:])) for b in pr(a)))
    k=[]
    for b in pr(a):
        t=sum((x-y) for x,y in zip(b,b[1:]))
        if t>=s:
            s=t
            # l=[list(b),s]
            k.append([list(b),s])
    k.sort(key=lambda x:-x[1])
    i=0
    while k[i][1]==k[0][1]:
        i+=1
    print(*k[i-1][0])