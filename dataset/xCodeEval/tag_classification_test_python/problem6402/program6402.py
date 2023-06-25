def program6402():
    n,k = map(int, input().split())
    if k!= 0:
      if n>=(3*k):
        print(min(1,n-k),2*k)
      else:
        print(min(1,n-k),(n-k))
    else:
      print(0,0)