def program4123():
    n,m=map(int,input().split())
    a=[[*input()]for _ in[0]*n]
    p=(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)
    for i in range(n-2):
     for j in range(m-2):
      if all(a[i+k][j+l]<'.'for k,l in p):
       for k,l in p:a[i+k][j+l]='$'
    print('YNEOS'['#'in sum(a,[])::2])