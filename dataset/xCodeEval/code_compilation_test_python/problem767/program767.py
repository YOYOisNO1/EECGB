def program767():
    vp = int(input())
    vd = int(input())
    t = int(input())
    f = int(input())
    c = int(input())
    s = t * vp
    td = t
    ans = 0
    vr = vd - vp
    while (vr > 0 and s < c):
        ttvr = s
        if s * vr + vp * ttvr >= c * vr: break
        ans += 1
        s = s * vr + vp * (2 * ttvr + f * vr)
        vp *= vr
        vd *= vr
        c *= vr
        vr *= vr
    print ans