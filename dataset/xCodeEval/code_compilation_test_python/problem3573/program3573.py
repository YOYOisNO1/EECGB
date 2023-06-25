def program3573():
    m = int(input())
    c = map(int, input().split())
    x, y = [int(i) for i in input().split()]
    
    cumFreq = [0]
    total = 0
    strong = 0
    LSum, RSum = 0, 0
    r = range(x, y+1)
    for i in c:
        total += i
        cumFreq.append(total)
    
    if max(x, y) * 2 < total:
        print(0)
    else:
        k = m//2
        LSum = cumFreq[k]
        RSum = total - LSum
        if LSum in r and RSum in r:
            print(k+1)
        else:
            print(LSum, RSum)
            if LSum > RSum:
                while not (LSum in r and RSum in r):
                    k -= 1
                    LSum = cumFreq[k]
                    RSum = total - LSum
            elif LSum < RSum:
                while not (LSum in r and RSum in r):
                    k += 1
                    LSum = cumFreq[k]
                    RSum = total - LSum
            if LSum in r and RSum in r:
                print(k+1)
            else:
                print(-1)