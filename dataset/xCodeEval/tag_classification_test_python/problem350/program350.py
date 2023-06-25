def program350():
    n = input()
    x = ""
    x += n[0]
    x += n[2]
    x += n[4]
    x += n[3]
    x += n[1]
    x = int(x)
    y = pow(x, 5)
    y = str(y)
    ans = ""
    ans += y[len(y)-5]
    ans += y[len(y)-4]
    ans += y[len(y)-3]
    ans += y[len(y)-2]
    ans += y[len(y)-1]
    print(ans)			
    # 6
    # 30 40 50 58 47