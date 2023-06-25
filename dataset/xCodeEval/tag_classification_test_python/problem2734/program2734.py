    # n,t=input().split(' ')
    # n=int(n)
    # t=int(t)
    # l=[]
    # for i in range(1,n+1):
    #     s,d=input().split(' ')
    #     s=int(s)
    #     d=int(d)
    #     l.append((s,d))
    
    n=int(input())
    a = list(map(int, input().split(' ')))
    if n==1:
        print(0)
    else:
    def sameItem (a):
            if len(a) < 1:
                return True
            return len(a) == a.count(a[0])
        D=-1
        if sameItem(a) == True:
            D=0
        a=set(a)
        a=sorted(a)
        if len(a)==2:
            if (a[1]+a[0])%2 == 0:
                D= ((a[1]+a[0])//2)-a[0]
            else:
                D=a[1]-a[0]
            # D=a[1]-a[0]
        elif len(a)==3:
            if (a[1]-a[0]) == (a[2]-a[1]):
                D=a[1]-a[0]
            else:
                D=-1
    
        print(D)
    