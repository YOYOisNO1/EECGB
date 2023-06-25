def program329():
    m, d = map(int, input().split())
    large_month = (1, 3, 5, 7, 8, 10, 12)
    small_month = (4, 6, 9, 11)
    leap_years = (2,)
    if m in large_month:
        if d >= 6:
            print(6)
        else:
            print(5)
    elif m in small_month:
        if d >= 7:
            print(6)
        else:
            print(5)
    elif m in leap_years:
        if d == 1:
            print(4)
        else:
            print(5)