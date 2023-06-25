def program1315():
    a = [int(x) for x in input().split()]
    buy = [int(x) for x in input().split()]
    sell= [int(x) for x in input().split()]
    buy.sort()
    sell.sort()
    MinBuy = min(buy)
    MaxSell = max(sell)
    BeginBourles = a[2]
    MaxBourles = 0
    if (MinBuy >= MaxSell):
        print(a[2])
        exit(0)
    k=0
    while (True):
        if (a[2]<buy[k] or k >= len(buy)):
            break;
        else:
            MaxBourles += a[2]//buy[k]
            a[2] %= buy[k]
            k +=1
    print(MaxBourles*MaxSell + a[2])
    