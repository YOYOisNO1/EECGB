def program1161():
    s = input().split(' ')
    d = int(s[0])
    sumtime = int(s[1])
    minsum = 0
    maxsum = 0
    mintime = []
    maxtime = []
    
    
    for i in range(d):
        s = input().split(' ')
        mintime.append(int(s[0]))
        maxtime.append(int(s[1]))
        minsum += mintime[i]
        maxsum += maxtime[i]
    
    if sumtime < minsum or sumtime > maxsum:
        print('NO')
    else:
        print('YES')
        sol = mintime
        left = sumtime - minsum
        i = 0
        while left != 0:
            dif = maxtime[i] - mintime[i]
            if left >= dif:
                sol[i] = maxtime[i]
                left -= dif
            else:
                sol[i] += left
                left = 0
            i += 1
        print(' ').join(str(s) for s in sol)