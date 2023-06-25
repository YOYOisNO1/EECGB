def program1166():
    import math
    
    slog = lambda x: math.log(math.log(x))
    a = [float(n) for n in input().split()]
    r = ([(lambda x, y, z: 0.0 if math.log(x) < 0 else slog(x) + z * math.log(y), "x^y^z"),
          (lambda x, y, z:0.0 if math.log(x) < 0 else slog(x) + y * math.log(z), "x^z^y"),
          (lambda x, y, z:0.0 if math.log(x) < 0 else slog(x) + math.log(y) + math.log(z), "(x^y)^z"),
          (lambda x, y, z:0.0 if math.log(y) < 0 else slog(y) + z * math.log(x), "y^x^z"),
          (lambda x, y, z:0.0 if math.log(y) < 0 else slog(y) + x * math.log(z), "y^z^x"),
          (lambda x, y, z:0.0 if math.log(y) < 0 else slog(y) + math.log(z) +  math.log(x), "(y^x)^z"),
          (lambda x, y, z:0.0 if math.log(z) < 0 else slog(z) + y * math.log(x), "z^x^y"),
          (lambda x, y, z:0.0 if math.log(z) < 0 else slog(z) + x * math.log(y), "z^y^x"),
          (lambda x, y, z:0.0 if math.log(z) < 0 else slog(z) +  math.log(y) + math.log(x), "(z^x)^y")])
    exp = ""
    if all([x < 1.0 for x in a]):
    	best = 10000000000000.3
    	for f, e in r:
    		val = f(1 / a[0], 1 / a[1], 1 / a[2])
    		if val < best:
    			best = val
    			exp = e
    else:
    	best = -10000000000000.3
        for f, e in r:
            val = f(a[0], a[1], a[2])
            if val > best:
                best = val
                exp = e
    
    print (exp)