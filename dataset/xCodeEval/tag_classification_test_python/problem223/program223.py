def program223():
    nums = list(map(int, input().split()))
    res = 0
    # print(len(nums))
    for i in range (0,len(nums)):
      copy_nums = nums[:]
      # compute the cost
      total_chunk = int(copy_nums[i]/len(nums))
      #print(total_chunk)
      total = int(copy_nums[i]%len(nums))
      #print(total)
      copy_nums[i] = 0
      for j in range(0,len(nums)):
        copy_nums[j] = copy_nums[j] + total_chunk
      next = (i+1)%len(nums)
      while total > 0:
        total = total -1
        copy_nums[next] = copy_nums[next] +1
        next = (next+1)%len(nums)
      wins = 0
      #print(copy_nums)
      for j in range (0,len(nums)):
        if copy_nums[j] %2 == 0:
          wins = wins + copy_nums[j]
      res = max(res, wins)
    print(res)