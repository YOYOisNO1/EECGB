def program3368():
    mod = 10 ** 9 + 7
    ii = lambda : int(input())
    si = lambda : input()
    dgl = lambda : list(map(int, input()))
    f = lambda : map(int, input().split())
    il = lambda : list(map(int, input().split()))
    ls = lambda : list(input())
    n=ii()
    x=int(n**0.5)
    s1=sum(2 if n%i==0 else 0 for i in range(1, x+1))
    print(s1-1 if x**2==n else s1)