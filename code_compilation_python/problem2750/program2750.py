def program2750():
    time = list(input())
    hh = time[0]
    hh += time[1]
    mm = time[3]
    mm += time[4]
    mm = str(int(mm) + 1)
    if mm == '60':
        mm = '00'
        if hh == '23':
            hh = '00'
        else:
            hh = str(int(hh) + 1)
    while hh != mm[::-1]:
        mm = str(int(mm)+1)
        if mm == '60':
            mm = '00'
            if hh == '23':
                hh = '00'
            else:
                hh = str(int(hh) + 1)
        if len(mm) == 1:
            mm = '0'+mm12:21
    print(hh+':'+mm,sep='')