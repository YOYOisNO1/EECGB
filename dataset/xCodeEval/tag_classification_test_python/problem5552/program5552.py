def program5552():
    import math
    x1, y1, r1, R1 = [int(i) for i in input().split(' ')]
    x2, y2, r2, R2 = [int(i) for i in input().split(' ')]
    d = math.sqrt((x1-x2)**2+(y1-y2)**2)
    
    s = 0
    f = lambda r1, r2, R2: (r1 + R2 <= d) or ((abs(r1 - r2) >= d) and ((r1 <= r2) or ((r1 >= R2) and abs(r1 - R2) >= d)))
    if f(r1, r2, R2):
        s+=1
    if f(R1, r2, R2):
        s+=1
    if f(r2, r1, R1):
        s+=1
    if f(R2, r1, R1):
        s+=1
    print(s)