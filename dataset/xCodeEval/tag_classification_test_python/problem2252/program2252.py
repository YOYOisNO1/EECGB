def program2252():
    n=int(input())
    x=map(int,input().split())
    s=set(x)-{0}
    print(len(s))