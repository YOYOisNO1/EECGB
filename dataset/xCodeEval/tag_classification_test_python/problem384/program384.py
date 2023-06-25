def program384():
    n, a, b, c = map(int, input().split())
    
    mins = dict()
    mins[0] = 0
    mins[1] = min(a, b + c, 3 * c)
    mins[2] = min(2 * mins[1], b, 2 * c)
    mins[3] = min(3 * mins[1], mins[1] + mins[2], c)
    
    rem = n % 4
    rest = 4 - rem if rem else 0
    print(mins[rest])