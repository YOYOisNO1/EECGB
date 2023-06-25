def program2852():
    # https://codeforces.com/problemset/problem/801/B
    # 900
    
    
    x = input()
    y = input()
    z = ""
    
    for i, xy in enumerate(zip(x, y)):
        xc, yc = xy
        xv = ord(xc)
        yv = ord(yc)
    
        if xv < yv:
            z = -1
            break
        
        z += yc
    
        
    
    print(z)