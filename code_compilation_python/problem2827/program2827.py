def program2827():
    # nums = input().split("\n")
    # drone = nums[0].split(" ")
    # flag = nums[1].split(" ")
    
    nums = input().split(" ")
    drone = nums[0:2]
    flag = nums[2:4]
    
    drone[0] = int(nums[0])
    drone[1] = int(nums[1])
    
    flag[0] = int(flag[0])
    flag[1] = int(flag[1])
    
    dist_x = abs(flag[0] - drone[0]) + 1
    dist_y = abs(flag[1] - drone[1]) + 1
    
    total_dist = dist_x * 2 + dist_y * 2
    
    print(total_dist)