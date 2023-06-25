def program446():
    I=lambda:map(int, input().split())
    r, h = I()
    ans = h / r * 2
    h = h - h / r * r
    if h * 2 < r: ans += 1
    elif h*2.0 >= (3.0**0.5)*r: ans += 3
    else: ans += 2
    print(ans)