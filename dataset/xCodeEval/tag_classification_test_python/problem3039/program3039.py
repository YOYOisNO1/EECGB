def program3039():
    import math
    from fractions import Fraction
    line = input()
    data = line.split()
    x1, y1 = float(data[0]), float(data[1])
    line = input()
    data = line.split()
    x2, y2 = float(data[0]), float(data[1])
    line = input()
    data = line.split()
    x3, y3 = float(data[0]), float(data[1])
    dis12 = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    dis23 = (x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)
    dis13 = (x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)
    '''
    print(dis12)
    print(dis13)
    print(dis23)
    '''
    cos1 = (dis13 + dis12 - dis23) / (2 * math.sqrt(dis12 * dis13))
    cos2 = (dis23 + dis12 - dis13) / (2 * math.sqrt(dis23 * dis12))
    cos3 = (dis13 + dis23 - dis12) / (2 * math.sqrt(dis13 * dis23))
    '''
    print('*',cos1)
    print('*',cos2)
    print('*',cos3)
    '''
    angle1 = math.acos(cos1) * 2
    angle2 = math.acos(cos2) * 2
    angle3 = math.acos(cos3) * 2
    '''
    print('#',angle1)
    print('#',angle2)
    print('#',angle3)
    '''
    number1 = Fraction.from_float(angle1 / angle2).limit_denominator(101)
    #print(number1.numerator)
    #print(number1.denominator)
    l1 = angle1 / number1.numerator
    #print(l1)
    n1 = 2 * math.pi / l1
    n1_int = int(n1 + 0.5)
    #print(n1_int)
    
    number2 = Fraction.from_float(angle1 / angle3).limit_denominator(101)
    #print(number2.numerator)
    #print(number2.denominator)
    l2 = angle1 / number2.numerator
    #print(l2)
    n2 = 2 * math.pi / l2
    n2_int = int(n2 + 0.5)
    #print(n2_int)
    
    if abs(n1_int - n1) < abs(n2_int - n2):
        n = n1_int
    else:
        n = n2_int
    
    sin1 = math.sqrt(1 - cos1 * cos1)
    #print(sin1)
    #print(dis23)
    r = math.sqrt(dis23) / (2 * sin1)
    #print(r)
    area = 1 / 2 * n * math.sin(2 * math.pi / n) * r * r
    print('%.6f' % area)