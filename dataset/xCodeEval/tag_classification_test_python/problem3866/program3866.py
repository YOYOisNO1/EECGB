def program3866():
    input()
    a=[0]+[*map(int,input().split())]+[1001]
    m=c=0
    for x,y in zip(a,a[1:]):c=(0,c+1)[x+1==y];m=max(m,c-1)
    print(m)