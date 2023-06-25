def program4515():
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    a=set(a)
    a=list(a)
    l=len(a)
    tag=[1 for i in range(l)]
    if (l==1):
        print(1)
    else:
        count=0
        for i in range(l):
            if (not tag[i]):
                continue
            tag[i]=0
            for j in range(l):
                if (a[j]%a[i]==0 and tag[j]):
                    tag[j]=0
            count+=1
        print(count)