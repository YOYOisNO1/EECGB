def program16():
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    if sum(l[:a-1])<=b:print("YES")
    else:print("NO")