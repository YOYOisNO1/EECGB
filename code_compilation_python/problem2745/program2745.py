def program2745():
    from datetime import date
    a = date(*map(int,input().split(':')))
    b = date(*map(int,input().split(':')))
    print(abs(a-b).days)