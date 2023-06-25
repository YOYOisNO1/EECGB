def program3484():
    d,c = map(int, input().split(' '))
    a = [int(x) for x in input().strip().split(' ')]
    rem = 0
    days=0
    for candles in a:
        #print(c)
        if candles >8:
            c-=8
            rem+=candles-8
            days+=1
        else:
            if rem+candles>8:
                c-=8
                rem-=8-candles
            else:
                c-=rem+candles
                rem = 0
            days+=1
        if c<=0:
            break
    if c>0:
        print("-1")
    else:
        print(days)