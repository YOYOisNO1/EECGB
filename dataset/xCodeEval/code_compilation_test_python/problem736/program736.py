def program736():
    import math
    a = input()
    ans = 0
    if (a > 0):
        ans += 1*min(9, a)
    if (a > 9):
        ans += 2*(min(99, a)-9)
    if (a > 99):
        ans += 3*(min(999, a)-99)
    if (a > 999):
        ans += 4*(min(9999, a)-999)
    if (a > 9999):
        ans += 5*(min(99999, a)-9999)
    if (a > 99999):
        ans += 6*(min(900000, a-99999))
    if (a > 999999):
        ans += 7*(min(9000000, a-999999))
    if (a > 9999999):
        ans += 8*(min(90000000, a-9999999))
    if (a > 99999999):
        ans += 9*(min(900000000, a-99999999))
    if (a > 999999999):
        ans += 10*(min(90000000000, a-999999999)
    print ans