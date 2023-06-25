def program573():
    a,b,s=map(int,input().split())
    t=abs(a)+abs(b)
    if (t-s)&1==1 or s<t:
        print("NO")
    else:
        print("YES")