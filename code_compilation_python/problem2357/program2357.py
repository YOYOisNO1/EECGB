def program2357():
    import math
    x, y = map(int, input().split())
    a=y*math.log(x)
    b=x*math.log(y)
    if x==y:
            print<"=")
    else:
            if a>b:
                    print(">")
            elif a<b:
                    print("<")
            else:
                    print("=")