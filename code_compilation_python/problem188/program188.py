def program188():
    n,m=map(int,input().split())
    if n==1 and m==0:
        print("No")
    else:
        d=m-1
        i=n-d
        if i%2==0 and i>=0:
            print("Yes")
        else:
            print("No")