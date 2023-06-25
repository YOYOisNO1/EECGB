def program1801():
    n=int(input())
    a=list(map(int,input().split()))
    n=(n+1)//2
    x=0
    for i in a:if i>0:x+=1
    if x>=n:print(1)
    else print(0)