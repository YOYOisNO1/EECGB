def program2747():
    import time
    a = input()
    b = input()
    ta = time.mktime(time.strptime(a, "%Y:%m:%d"))
    tb = time.mktime(time.strptime(b, "%Y:%m:%d"))
    d = abs(ta-tb) / 3600 / 24
    print(round(d))