def program1715():
    n = int(input())
    lst = [int(x) for x in input().split()]
    res = []
    for i in range(n-1, -1, -1):
      if lst[i] not in res:
        res.append(lst[i])
    print(len(res))
    for i in range(len(res)-1, -1, -1):
      print(res[i], end=" ")