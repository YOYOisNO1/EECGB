def program1278():
    for _ in range(int(input())):
      n,m=[map(int,input().split()]
      x=((2**m)-1)
      res=(x**n)%1000000007
      print(res)