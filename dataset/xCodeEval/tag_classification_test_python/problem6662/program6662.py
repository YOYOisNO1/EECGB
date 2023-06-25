def program6662():
    import fractions
    
    n, m, x, y, a, b = (int(x) for x in input().split())
    
    g = fractions.gcd(a, b)
    a /= g
    b /= g
    
    z = min(n / a, m / b)
    
    w = a * z
    h = b * z
    
    min_left = max(0, x - w)
    max_left = min(x, n - w)
    optimal_left = x - (w + 1) / 2
    
    left = None
    if max_left < optimal_left:
      left = max_left
    elif min_left > optimal_left:
      left = min_left
    else:
      left = optimal_left
    
    min_bottom = max(0, y - h)
    max_bottom = min(y, m - h)
    optimal_bottom = y - (h + 1) / 2
    
    bottom = None
    if max_bottom < optimal_bottom:
      bottom = max_bottom
    elif min_bottom > optimal_bottom:
      bottom = min_bottom
    else:
      bottom = optimal_bottom
    
    print(left,) bottom, left + w, bottom + h