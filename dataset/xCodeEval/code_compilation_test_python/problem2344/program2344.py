def program2344():
    n,k=map(int,input().split()))
    for i in range(n+1):
      if 3*(n-i)<=k-2*i<=5*(n-i):
        print(i)
        break