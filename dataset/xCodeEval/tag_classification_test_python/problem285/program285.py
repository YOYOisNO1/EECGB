def program285():
    n, m = map(int,input().split())
    s = list(map(int , input().split()))
    st = list(set(s))
    if len(st) >= m:
      print("YES")
      for i in range(m):
        print(s.index(st[i])+1 , end =' ')
    else :
      print("NO")   
     