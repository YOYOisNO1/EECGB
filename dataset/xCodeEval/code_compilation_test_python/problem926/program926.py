def program926():
    readints=lambda:map(int, input().strip('\n').split())
    n,m=readints()
    a=list(readints())
      
    a.sort()
    a.pop()
    
    if not a or sum(a)<=m:
      print(‘YES’)
    else:
      print(’NO’)