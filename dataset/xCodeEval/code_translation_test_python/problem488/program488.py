def program488():
    from math import log
    x, y = map(int, input().split())
    
    if (log(x)/x == log(y)/y):
        print("=")
    elif (log(x)/x  > log(y)/y):
        print(">")
    else:
        print("<")