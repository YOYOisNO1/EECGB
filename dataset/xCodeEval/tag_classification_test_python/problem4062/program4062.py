def program4062():
    #wtf is this, please dont judge me
    
    i = int(input())
    nums = {}
    while i>0:
    	n = int(input())
    	if n in nums:
    		nums[n]+=1
    	else:
    		nums[n]=1
    	i-=1
    # print(nums)
    if len(nums) == 2 and nums.values()[0] == nums.values()[1]:
    	print("YES")
    	print("%d %d") % (nums.keys()[0],nums.keys()[1])
    else:
    	print("NO")