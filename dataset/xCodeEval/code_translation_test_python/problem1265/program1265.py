def program1265():
    n = -input() % 360
    
    if n == 0:
        print(0)
    else:
        ans = 0
        pos = min(abs(360 - n) ,abs(-n))
    
        for i in range(1,4):
            if min(abs(360 - (n + 90 * i)),abs(- (n + 90 * i))) < pos:
                ans = i
                pos = min(abs(360 - (n + 90 * i)),abs(- (n + 90 * i)))
    
        print(ans)
        