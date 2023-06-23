def zero_based(hour):
        return hour if hour < 12 else 0
    
    h, m, s, t1, t2 = map(int, input())
    h = zero_based(h)
    t1 = zero_based(t1)
    t2 = zero_based(t2)
    t1, t2 = sorted([t1, t2])
    
    h *= 5
    t1 *= 5
    t2 *= 5
    can_reach = False
    
    if t2 > h and h > t1:
        can_reach = t2 > m and m > t1 and t2 > s and s > t1
    else:
        can_reach = not(t2 > m and m > t1) and not(t2 > s and s > t1)
    
    print('YES' if can_reach else 'NO')