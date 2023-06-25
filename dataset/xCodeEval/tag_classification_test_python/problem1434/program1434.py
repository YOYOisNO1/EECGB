def program1434():
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    res = 0
    index = -1
    for i in range(n):
      temp = a[i]//m
      if a[i] > m and a[i]%m != 0:
        temp += 1
      if res <= temp and a[i]>m:
        res = temp
        index = i+1
        
    if index == -1:
      index = n
    print(index)