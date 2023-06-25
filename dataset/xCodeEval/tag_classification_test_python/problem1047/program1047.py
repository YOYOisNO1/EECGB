def program1047():
    n=int(input())
    l=list(map(int,input().split()))
    d=list(map(int,input().split()))
    mm=min(l[0],d[1])+min(l[1],d[2])+min(d[0],l[2])
    x=min(l[0],n-d[1])+min(l[1],n-d[2])+min(l[2],n-d[0])
    print(n-x,mm)