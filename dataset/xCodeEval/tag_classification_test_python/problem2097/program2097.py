def program2097():
    nums = map(int, input('').split(' '))
    n, k, d = nums[0], nums[1], nums[2]
    ans = [(0, 0)] * 101
    
    
    ans[0] = (0, 1)
    for i in xrange(1, n + 1):
        num_contain = 0
        num_not_contain = 0
        for j in xrange(1, k + 1):
            if (i - j) >= 0:
                num_contain += ans[i - j][0]
                if j >= d:
                    num_contain += ans[i - j][1]
                else:
                    num_not_contain += ans[i - j][1]
        ans[i] = (num_contain, num_not_contain)
    print(ans[n][0]) % 1000000007