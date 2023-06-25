def program8016():
    # a,b,x,y  =map(int,input().split())
    # poly = a+b
    # vasily = max(x,y)
    # print(poly,vasily)
    # if poly-vasily>1:
    #   print("Vasiliy")
    # else:
    #   print("Polycarp")
    
    xp, yp, xv, yv = map(int, input().split())
    
    print('Polycarp') if (xp + yp) <= max(xv, yv) or (xp <= xv and yp <= yv) else 'Vasiliy'