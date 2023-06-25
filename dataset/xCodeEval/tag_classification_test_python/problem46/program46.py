def program46():
    import sys
     
     
     
    n,m,k=map(int, sys.stdin.readline().strip().split())
    if m >= n and k >= n:
        print("Yes")
    else:
        print("No")