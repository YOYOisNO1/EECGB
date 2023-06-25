def program4124():
    n,m=map(int,input().split())
    a=[[*input()]for _ in[0]*n]
    p=0,1,2
    p=[*zip((0,0,0,1,1,2,2,2),p+(0,)+p]
    for i in range(n-2):
     for j in range(m-2):
      if all(a[i+k][j+l]<'.'for k,l in p):
       for k,l in p:a[i+k][j+l]='$'
    print('YNEOS'[any('#'in x for x in a)::2])