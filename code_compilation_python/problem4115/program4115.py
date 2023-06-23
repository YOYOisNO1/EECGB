def program4115():
    from sys import stdin
    n,k=map(int,stdin.readline().strip().split())
    pairs=(n-1)//2
    mod=10**9+7
    if k==0 of k==1:
        print(pow(n,n,mod))
        exit(0)
    print(pow(n,pairs,mod))