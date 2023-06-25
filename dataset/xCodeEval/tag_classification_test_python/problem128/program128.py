    import sys
    
    for line in sys.stdin:
            n = int(line)
    
    
    intlist = []
    maxcount = 0
    fintlist = []
    
    i = 1
    while i <= n:
            intlist.append(1)
            i = i + 1
    
def rec_fn(rn,rint_list,mcount):
            j = 0
            lastz = -1
            while j < n:
                    if rint_list[j] == 1:
                            if rn - j - 1 == 0:
                                    mcount += 1
                                    rint_list[j] = 0
                                    global maxcount
                                    if maxcount < mcount:   
                                            maxcount = mcount
                                            global fintlist
                                            fintlist = list(rint_list)
                                    break
                            if rn - j - 1 > 0:
                                    mcount += 1
                                    rint_list[j] = 0
                                    j += 1
                                    rec_fn(n,rint_list,mcount)
                                    break;
                            else:
                                    rint_list[lastz] = -1
                                    rec_fn(n,rint_list,mcount - 1)
                                    break;
                    elif rint_list[j] == 0:
                            lastz = j
                            rn = rn - j - 1
                            j += 1
                    else:
                            j += 1
    
    
    rec_fn(n,intlist,0)
    print(maxcount)
    i = 0
    s = ''
    while i < len(fintlist):
            if fintlist[i] == 0:
                    s +=  str(i + 1) + ' '
            i += 1
    print(s)