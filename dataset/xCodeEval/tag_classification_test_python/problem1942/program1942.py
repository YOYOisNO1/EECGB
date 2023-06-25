def f(da, db):
        if da == 9 and db == 1:
            return "999 1000"
        if da > db: return -1
        if abs(da - db) > 1: return -1
        elif abs(da - db) == 0:
            return "{} {}".format(da * 100, (db * 100) + 1)
        else:
            return "{} {}".format(str(da) + "99", str(db) + "00")
    
    
    da, db = [int(i) for i in input().split()]
    
    print(f(da, db))