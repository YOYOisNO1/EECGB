def program1070():
    n,k=map(int,input().split())
    r=n/k
    if r%2==1:
        print("YES")
    else:
        print("NO")