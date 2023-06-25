def program35():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    s = a*1000+b*100+c*10+d
    if s == 0:
        print(0) #OK2
    elif s == 1:
        print(0/0)
    elif s == 10:
        print(0/0)
    elif s == 11:
        print(1/(1-1))
    elif s == 100:
        print(1/(1-1))
    elif s == 101:
        print(1/(1-1))
    elif s == 110:
        print(0) #OK1
    elif s == 111:
        print(0)
    elif s == 1000:
        print(1)#OK3
    elif s == 1001:
        print(0)
    elif s == 1010:
        print(0)
    elif s == 1011:
        print(0)#<<
    elif s == 1100:
        print(0)
    elif s == 1101:
        print(0)
    elif s == 1110:
        print(0)
    elif s == 1111:
        print(0)