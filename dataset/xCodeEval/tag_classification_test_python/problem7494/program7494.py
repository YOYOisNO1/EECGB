def program7494():
    a, b, m = map(float, input().split())
    vx, vy, vz = map(float, input().split())
    t = m / -vy
    x = a / 2 + vx * t
    z = vz * t
    
    x = abs(x)
    z = abs(z)
    if int(x/a) % 2 == 1:
    	x = a - x % a
    else:
    	x = x % a
    
    if int(z / b) % 2 == 1:
    	z = b - z % b
    else:
    	z = z % b
    print(x,) z