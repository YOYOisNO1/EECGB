def program6087():
    x1 , y1 , x2 , y2 = map(int,input().split())
    dx = x2 - x1
    dy = y2 - y1
    ans = 0
    ans += ((dx + 2)//2)*((dy + 2)//2)
    ans += ((dx + 1)//2)*((dy)//2)
    print(ans)