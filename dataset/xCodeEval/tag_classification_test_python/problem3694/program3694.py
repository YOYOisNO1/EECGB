def program3694():
    n,m = map(int,input().split(' '))
    arr = [int(i) for i in input().split(' ')]
    
    for i in range(n):
      arr[i] = (arr[i],i+1)
    arr.sort()
    
    res = []
    for i,j in arr :
      if(m >= i):
        m -= i
        res.append(j)
    
    print(len(res))
    for i in res:
      print(i, end=' ')
    