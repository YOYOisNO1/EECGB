def program4347():
    from fractions import Fraction
    
    a, b, m = map(int, input().split(' '))
    x, y, z = map(int, input().split(' '))
    
    cx, cy, cz = Fraction(a / 2), Fraction(m), Fraction(0)
    
    while cy > 0:
        if cx == 0:
            x = abs(x)
        elif cx == a:
            x = -abs(x)
    
        if cz == 0:
            z = abs(z)
        elif cz == b:
            z = -abs(z)
    
        if x > 0:
            time_x = (a - cx) / x
        else:
            time_x = cx / -x
    
        time_y = -cy / y
    
        if z > 0:
            time_z = (b - cz) / z
        else:
            time_z = cz / -z
    
        time = min(time_x, time_y, time_z)
    
        cx += time * x
        cy += time * y
        cz += time * z
    
    print(float(cx), float(cz))