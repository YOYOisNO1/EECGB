def program2824():
    n=input()
    a=map(int,input().split())
    print max(a[:i].count(0)+a[i:].count(1) for i in range(n+1))