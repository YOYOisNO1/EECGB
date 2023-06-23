def program1167():
    import math
    
    a = [float(n) for n in input().split()]
    r = ([((lambda x, y, z: math.log(x) * y**z, "x^y^z"),
          (lambda x, y, z: math.log(x) * z**y, "x^z^y"),
          (lambda x, y, z: math.log(x) * y * z, "(x^y)^z"),
          (lambda x, y, z: math.log(y) * z ** y, "y^x^z"),
          (lambda x, y, z: math.log(y) * x ** z, "y^z^x"),
          (lambda x, y, z: math.log(y) * x * z, "(y^x)^z"),
          (lambda x, y, z: math.log(z) * x**y, "z^x^y"),
          (lambda x, y, z: math.log(z) * y**x, "z^y^x"),
          (lambda x, y, z: math.log(z) * x * y, "(z^x)^y")])
    
    best = -10000000000000.3
    exp = ""
    
    for f, e in r:
        val = f(a[0], a[1], a[2])
        if val > best:
            best = val
            exp = e
    
    print (exp)
    