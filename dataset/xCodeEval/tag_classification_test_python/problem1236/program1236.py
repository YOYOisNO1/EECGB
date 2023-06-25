def program1236():
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    
    week_a = int(a / 3)
    week_b = int(b / 2)
    week_c = int(c / 2)
    
    ids = [0, 1, 2, 0, 2, 1, 0]
    
    min_weeks = min(week_a, week_b, week_c)
    total_days = 7 * min_weeks
    a -= min_weeks * 3
    b -= min_weeks * 2
    c -= min_weeks * 2
    
    max_cur = 0
    for i, d in enumerate(ids):
        rem = [a, b, c]
        day = i
        cur = 0
        while rem[0] >= 0 and rem[1] >= 0 and rem[2] >= 0:
            if rem[ids[day % 7]] == 0:
                break
            rem[ids[day % 7]] -= 1
            cur += 1
            day += 1 
        if cur > max_cur:
            max_cur = cur
    
    print(total_days + max_cur)