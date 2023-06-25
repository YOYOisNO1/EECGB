def program3029():
    //WeirdBugsButOkay
    
    s = input()
    t = input()
    
    unk = 0
    acp = 0
    cp = 0
    for i in range (0,len(s)) :
        if t[i] == '?' :
            unk += 1
        elif t[i] == '+' :
            acp += 1
        else :
            acp -= 1
        if s[i] == '+' :
            cp += 1
        else :
            cp -= 1
    ans = 0
    if cp - unk > acp or cp + unk < acp :
        print('%0.11f'%0)
    elif unk == 0 :
        if cp == acp :
            print('%0.11f'%1)
        else :
            print('%0.11f'%0)
    else :
        ct = cp - acp
        if ct % 2 != 0 :
            print('%0.11f'%0)
        else :
            cnt = (ct + unk) // 2
            ncr = 1
            for i in range (0, cnt) :
                ncr *= (unk - i)
                ncr //= (i + 1)
            ans = ncr
            ans /= (2**unk)
            print('%0.11f'%ans)