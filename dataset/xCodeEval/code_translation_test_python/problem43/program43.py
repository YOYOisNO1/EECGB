def Spider ():
        a, b, c, d = map(int, input().split())
        if b >= a: print("Second")
        else: print("First")
    TIMES = 1
    #TIMES = int(input())
    for TIME_TEMP in range(TIMES):
        Spider()