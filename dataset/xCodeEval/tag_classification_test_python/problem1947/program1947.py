def program1947():
    n,na,nx=list(map(int,input().strip().split()))
    l=list(map(int,input().strip().split()))
    t=list(map(int,input().strip().split()))
    for j in range(1,n+1):
        if j in l:
            print("1",end=" ")
        elif j in t:
            print("2",end=" ")
    print()