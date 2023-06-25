    import math
    import sys
    
def get_next(x):
        t = (-3 + math.sqrt(12 * x - 3)) / 6.0
        t = math.floor(t)
        for i in range(max(t - 6, 1), t + 7):
            nx = x + i ** 3
            if nx < (i + 1) ** 3:
                return nx
        assert(False)
    
    min_by_level = [0, 1]
    for i in range(2, 20):
        min_by_level.append(get_next(min_by_level[-1]))
    
    high = int(input())
    level = 1
    while min_by_level[level] <= high:
        level += 1
    level -= 1
    
    ans_level = level
    ans_number = 0
    
    for i in range(level - 1, -1, -1):
        le = 1
        rg = 10 ** 5 + 1
        while rg - le > 1:
            mid = (rg + le) // 2
            if high - mid ** 3 >= min_by_level[i]:
                le = mid
            else:
                rg = mid
    
        ans_number += le ** 3
        high = min(high - le ** 3, (le + 1) ** 3 - 1 - le ** 3)
    
    
    print(ans_level, ans_number)