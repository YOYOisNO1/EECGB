    n = int(input())
    
def sum_num(n):
      return sum([int(c) for c in str(n)]) 
    
    assert(sum_num(15) + 15 == 21)
    
    nums = []
    for i in range(max(n-9*len(str(n)),0),n):
      if i + sum_num(i) == n:
        nums.append(i)
    
    if len(nums) > 0:
      print(len(nums))
      for i in nums:
        print(i)
    else:
      print(0)
    
    