def program1108():
    n,a,b = map(int,input().split())
    a,b = (min(a,b)),max(a,b)
    maxst = 0
    while n != 1:
        maxst += 1
        n //= 2
    tmp = b - a
    curst = 0
    while tmp != 1:
        curst += 1
        tmp //= 2
    if (curst + 1 == maxst):
        print('Final!')
    else:
        print(curst + 1)