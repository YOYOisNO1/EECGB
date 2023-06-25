def program1189():
    l,r,a = map(int, input().split())
    c = 0
    left = 0
    if l < r:
        c = c + 2*l
        r = r - l
        left = r
    else:
        c = c + 2*r
        l = l - r
        left = l
    if a >= left:
        c = c + 2*left
        a = a - left
        left = 0
    else:
        c = c + 2*a
        left = left - a
        a = 0
    if a > 0:
        c = c + 2*(a//2)
    print(c)