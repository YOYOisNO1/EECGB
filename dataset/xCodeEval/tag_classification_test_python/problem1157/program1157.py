def program1157():
    
    
    temp = input().split()
    d, st = int(temp[0]), int(temp[1])
    
    maxt = []
    mint = []
    
    for _ in range(d):
        temp = input().split()
        mint.append(int(temp[0]))
        maxt.append(int(temp[1]))
    
    maxs, mins = sum(maxt), sum(mint)
    
    if mins <= st <= maxs:
        print('YES\n')
        st -= mins
        for i in range(d):
            print(mint[i]+min(st,maxt[i]-mint[i]))
            st -= min(st,maxt[i]-mint[i])
        print('\n')
    else:
        print('NO\n')