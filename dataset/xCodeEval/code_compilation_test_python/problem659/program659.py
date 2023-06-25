def program659():
    
     from sys import stdin
    import math
    
    line = stdin.readline().rstrip().split()
    l = int(line[0])
    r = int(line[1])
    x = int(line[2])
    y = int(line[3])
    
    
    
    w = x * y
    
    maxN = min(min(r, y), math.floor(math.sqrt(w)))
    count = 0
    
    if y%x != 0:
        print(0)
    else:
        for a in range(l, maxN+1):
            if w % a == 0:
                b = int(w/a)
                if a >= l and a <= r and b >=l and b <= r:
                    if a % x == 0 and b % x == 0 and y % a == 0 and y % b == 0:
                        gcd = math.gcd(int(a/x), int(b/x))
                        if gcd == 1:
                            if a != b:
                                count += 1
                            count += 1
        print(count)