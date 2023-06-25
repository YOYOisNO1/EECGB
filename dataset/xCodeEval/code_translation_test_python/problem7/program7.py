def program7():
    M = 100000
    
    I = lambda:map(int, input().split())
    
    data = []
    
    for i in range(3):
        data.append(I())
    
    a = sum(data[0])
    b = sum(data[1])
    c = sum(data[2])
    
    # x + a = y + b = z + c
    m = min(a, b, c)
    data[0][0] = (b + c - a)/2
    data[1][1] = (c + a - b)/2
    data[2][2] = (a + b - c)/2
    
    for d in data:
        for v in d:
            print(v,)
        print('')