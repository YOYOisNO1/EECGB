def program97():
    a,h,k=map(int,input().split())
    g,p,b=map(int,input().split())
    if(a>g or h>((g-a)+p) or k>((g-a)+(p-h)+b)):
        print("NO")
    else:
        print("YES")
        