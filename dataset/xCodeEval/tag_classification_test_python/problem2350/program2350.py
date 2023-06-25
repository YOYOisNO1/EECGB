def program2350():
    #import sys
    #sys.stdin = open('in')
    
    n = int(input())
    
    ok = False
    for i in range(4):
        nums = map(int,input().split())
        if not ok:
            if min(nums[0], nums[1]) + min(nums[2], nums[3]) <= n:
                print(str(i) +1) + ' ' + str(min(nums[0], nums[1])) + ' ' + str(n - min(nums[0], nums[1]))
                ok = True
    if not ok:
        print(-1)