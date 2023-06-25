def program270():
    from datetime import datetime
    date_format = "%Y:%m:%d"
    x= input()
    y= input()
    a = datetime.strptime(x, date_format)
    b = datetime.strptime(y, date_format)
    delta = b - a
    print(abs(delta.days)) # that's it