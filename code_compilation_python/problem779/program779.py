def program779():
    n,k = map(int, input().split())
    print(n+(n%k)+(k if n%k==0))