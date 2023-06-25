def program1036():
    N1 , N2 = map(int, input().split())
    count2 = 0
    count3 = 0
    for i in range(N1, N2 + 1):
        if i%2 == 0:
            count2 = count2+1
            
        elif i%3 == 0:
            count3 = count3 + 1
    if count2 > count3:
        print 2
    else:
        print 3