def program1450():
    import sys
    
    a,b,c,d = map(int,sys.stdin.readline().split())
    if 3*a/10 > a-a*c/250:
        misha = 3*a/10
    else:
        misha = a-a*c/250
    if 3*b/10 > b-b*d/250:
        vasya = 3*b/10
    else:
        vasya = b-b*d/250
    if misha>vasya:
        print('Misha')
    elif vasya>misha:
        print('Vasya')
    else:
        print('Tie')