def program8014():
    xp, yp, xv, yv = map(int, input().split())
    
    print('Polycarp') if (xp + yp) <= max(xv, yv) or (xp <= xv and yp <= yv) else 'Vasiliy'