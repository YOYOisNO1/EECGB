def program1235():
    a=[[0]*11 for _ in range(11)]
    n,a[0][0]=map(int,input().split())
    z=0
    a[0][0]*=1024
    #print(a)
    for r in range(n):
      for c in range(r+1):
        d=a[r][c]-1024
        if d>=0:
          z+=1
          a[r+1][c]+=d/2
          a[r+1][c+1]+=d/2
    #print(a)
    print(z)