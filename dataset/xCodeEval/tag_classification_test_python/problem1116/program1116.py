def program1116():
    n=int(input())
    a1,a2,a3=map(int,input().split())
    b1,b2,b3=map(int,input().split())
    minwin=n-(min(a1,b1+b3))-(min(a2,b1+b2))-(min(a3,b2+b3))
    maxwin=min(a1,b2)+min(a3,b1)+min(a2,b3)
    print(minwin,maxwin)