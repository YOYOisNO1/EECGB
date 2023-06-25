def program2954():
    s = input()
    a ,b = s.split()
    a = int(a)
    b = int(b)
    ans = pow(a*a+b*b,0.5) % 2
    #print(ans)
    if ans >1.0:
        res = False
    else:
        res = True
    if a * b > 0:
        res = not res
    if a == 0 or b == 0:
        res = False
    if ans % 1 == 0.0:
        res = False
    if res:
        print('white')
    else:
        print('black')