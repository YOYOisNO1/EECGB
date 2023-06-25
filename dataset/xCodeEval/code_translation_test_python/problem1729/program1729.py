def program1729():
    import sys
    
    (n, k) = input().split(' ')
    series = str(input())
    n = int(n)
    k = int(k)
    
    streak = False
    max_streak = 0
    curr_count = 0
    
    for i in xrange(n):
        if series[i] == 'N':
            if not streak:
                curr_count = 1
                streak = True
            else:
                curr_count += 1
        else:
            streak = False
            if max_streak < curr_count:
                max_streak = curr_count
    
    if max_streak < curr_count:
        max_streak = curr_count
    
    if int(k) < max_streak:
        print('NO')
        sys.exit()
    else:
        for i in xrange(n - k + 1):
            check_bounds = True
    
            # print(series[i:i+k])
            check = True
            for j in range(i, i+k):
                if not (series[j] == 'N' or series[j] == '?'):
                    check = False
                    break
            if check:
                if i != 0:
                    if series[i - 1] == 'N':
                        check_bounds = False
                        # print('left')
                if i != n - k:
                    if series[i + k] == 'N':
                        check_bounds = False
                        # print('right')
    
            if check and check_bounds:
                print('YES')
                sys.exit()
        print('NO')
        sys.exit()