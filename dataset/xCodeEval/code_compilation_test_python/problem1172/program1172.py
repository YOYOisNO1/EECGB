def program1172():
    a, b, c = map(int, input().split())
    d = b - a
    if a == b or (c != 0 and d*c > 0 and d%c == 0)):
        #d*c>0 either both increasing or both decreasing..
        #if c is positibe means increasing seq and b is negative so they can be met
        print("YES")
    else:
        print("NO")