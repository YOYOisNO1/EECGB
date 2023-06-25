def program2221():
    #!/usr/bin/env python3
    
    mp = []
    for ii in range(11):
        if ii==3 or ii==7:
            input()
            continue
        mp.append(list("".join([str(i) for i in input().split(' ')])))
    y,x = [int(i) for i in input().split(' ')]
    
    r = y%3
    c = x%3
    
    cnt = 0
    rr = (3+r-1)%3
    cc = (3+c-1)%3
    for i in range(3):
        for j in range(3):
            if mp[rr*3+i][cc*3+j]=='.':
                mp[rr*3+i][cc*3+j] = '!'
                cnt += 1
    if cnt==0:
        for i in range(9):
            for j in range(9):
                if mp[i][j]=='.':
                    mp[i][j] = '!'
    
    for i in range(9):
        if i==3 or i==6:
            print("")
        for j in range(9):
            if j==3 or j==6:
                print(" ",end='')
            print((mp[i][j],end=''))
            if j==8:
                print("")