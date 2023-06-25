def program2503():
    
    a, b, c = [int(x) for x in input("").split(" ")]
    
    out = "NO"
    if c != 0:
        if (b - a) / c > 0:
            if (b - a) % c == 0:
                out = "YES"
    
    if a == b:
        out = "YES"
    
    print(out)
    
    