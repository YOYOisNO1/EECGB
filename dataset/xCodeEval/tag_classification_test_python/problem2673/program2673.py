    import sys
    
def next_t(a, b):
        b += 1
        if b >= 60:
            a += 1
            b = 0
        if a >= 24:
            a = 0
    
        return (a, b)
    
def is_paly(a, b):
        a, b = str(a).zfill(2), str(b).zfill(2)
        return a[::-1] == b
    
    t = sys.stdin.readline().strip()
    a, b = tuple(int(x) for x in t.split(":"))
    
    (a, b) = next_t(a, b)
    while not is_paly(a, b):
        a, b = next_t(a, b)
    print(str(a).zfill(2) + ":" + str(b).zfill(2))