def program2636():
    c, str1, str2, a, differ = map(int, input().split(" "))
    
    days = 0
    
    while c > 0:
        if days > 0:
        c += differ
        c -= str1
        v0 += a
        if v1 < v0:
        str1 = str2
        days += 1
    
    print(days)