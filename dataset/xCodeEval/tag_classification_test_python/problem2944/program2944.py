def program2944():
    n = int(input())
    counter = 0
    nums = 19
    
    while counter < n:
        if sum([int(i) for i in str(nums)]) == 10:
            counter += 1
        nums += 9
    
    print(nums - 9)