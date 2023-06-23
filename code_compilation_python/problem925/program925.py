def program925():
    n,m=int(input()),int(input())
    a=[]
    for _in range(n):
      x=int(input())
      a.append(x)
      
    a.sort()
    a.pop()
    
    if not a or sum(a)<=m:
      print(‘YES’)
    else:
      print(’NO’)