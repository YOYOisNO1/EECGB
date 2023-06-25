def program3383():
    n,k=map(int,input().split())
    moves = n/k
    if moves%2==0:
        print("NO")
    else:
        print("YES")