def program215():
    mod = 1000000007
    ii = lambda : int(input())
    si = lambda : input()
    dgl = lambda : list(map(int, input()))
    f = lambda : map(int, input().split())
    il = lambda : list(map(int, input().split()))
    ls = lambda : list(input())
    f1,f2=f()
    n=ii()
    l=[f1,f2]
    temp=f2
    f2=f2-f1
    f1=temp
    for i in range(4):
        l.append(f2)
        temp = f2
        f2 = f2 - f1
        f1 = temp
    #print(*l)
    print(l[(n-1)%6]%mod)