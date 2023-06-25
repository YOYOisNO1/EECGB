def program2747():
    y = int(input())
    k = 0
    i = 0
    v = 0
    if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
        v = 1
    while True:
        i += 1
        if ((y + i) % 400 == 0) or (((y + i) % 4 == 0) and ((y + i) % 100 != 0)):
            k += 366
            vn = 1
        else:
            k += 365
            vn = 0
        if (k % 7 == 0) and (v == vn):
            break
    print((y) + i)