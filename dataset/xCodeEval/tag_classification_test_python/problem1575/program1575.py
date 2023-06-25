def program1575():
    k = int(input())
    arr = list(map(int, input().split()))
    
    answer = []
    sortedArr = sorted(arr, reverse=True)
    
    total = 0
    months = 0
    
    for i in range(12):
      if (total >= k):
        break
      else:
        total += sortedArr[i]
        months += 1
    
    if (months == 12 and total < k):
      print(-1)
    else:
      print(months)