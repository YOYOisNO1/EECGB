    import math
def amr_pins():
        r, sx, sy, fx, fy = map(int, input().strip().split())
        d = ((fx - sx) ** 2 + (fy - sy) ** 2) ** 0.5
        print int(math.ceil(d / (2 * r))
    
    amr_pins()