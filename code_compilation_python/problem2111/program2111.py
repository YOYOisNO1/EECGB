def program2111():
    #这题对0就等于求最大子段和
    
    n = int(input())
    nums = list(map(int, input().split()))
    nums_ = []
    count = []
    nums2 = point = index1 = index2 = 0
    num = []
    
    for i in range(len(nums)):
        if nums[i] == 0:
            nums_.append(1)
        else:
            nums_.append(-1)
        count.append(max(int(nums_[i])+nums2, int(nums_[i])))
        if int(nums_[i] >= int(nums_[i]+nums2)):
            nums2 = 0
            nums2 += int(nums_[i])
        else:
            nums2 += int(nums_[i])
    
    index2 = count.index(max(count)) #找出最大的数的位置
    
    num = list(range(index2+1))
    num.reverse()
    for i in num:
        if count[i] == 1:
            index1 = i
            break
    
    if index1 != 0:
        for j in range(index1):
            point += int(nums[j])
    if index2 != n:
        for p in range(n-index2-1):
            point += int(nums[p+index2+1])
    for q in range(index1,index2+1):
        point += int(1-nums[q])
    
    print(point)