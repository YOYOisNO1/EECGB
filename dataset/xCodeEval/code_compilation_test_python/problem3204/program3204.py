def program3204():
    R = lambda:map(int,input().split())＃
    #R = lambda:[30, 5, 20, 20, 5, 3]
    #R = lambda:[64, 12, 258, 141, 10, 7]
    
    x, t, a, b, da, db = R()
    
    for i in range(-1, t):
        if i == -1:
            sum_a = 0
        else:
            sum_a = a - da*i
        if sum_a < 0:
            sum_a = 0
    
        for j in range(-1, t):
            if j == -1:
                sum_b = 0
            else:
                sum_b = b - db*j
            if sum_b < 0:
                sum_b = 0
    
            if sum_a + sum_b == x:
                print 'YES'
                quit()
    print 'NO'