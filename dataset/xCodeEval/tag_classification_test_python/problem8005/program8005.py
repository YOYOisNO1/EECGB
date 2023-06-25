def program8005():
    xp, yp, xv, yv = map(int, input().split())
    if (max(xv, yv) >= (xp + yp)) or ((xv >= xp) and (yv >= yp)): print("Polycarp")
    else: print("Vasiliy")