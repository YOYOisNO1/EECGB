def program1180():
    mod = 1000000007
    ii = lambda : int(input())
    si = lambda : input()
    dgl = lambda : list(map(int, input()))
    f = lambda : map(int, input().split())
    il = lambda : list(map(int, input().split()))
    ls = lambda : list(input())
    n,x,y=f()
    l=[n//2,n//2+1]
    if x in l and y in l:
        print('NO')
    else:
        print('YES')