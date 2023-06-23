def program927():
    readi=lambda: map(int, input().strip(‘\n’).split())
    n,m=readi()
    a=list(readi())
      
    a.sort()
    a.pop()
    
    if not a or sum(a)<=m:
      print(‘YES’)
    else:
      print(’NO’)