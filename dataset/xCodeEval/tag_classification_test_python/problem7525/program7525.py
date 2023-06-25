def program7525():
    n,m=map(int,input().split())
    x=input()-1
    print(max(n+m-4*x-2,1)) if min(n,m)>2*x else 0