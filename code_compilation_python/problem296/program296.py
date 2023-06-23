def program296():
    s=[None,None,None]
    for i in range(3):
        s[i]=input()
    n={'0':0,'X':0,'.':0}
    for i in range(3):
        for j in range(3):
            n[s[i][j]]+=1
    if n['0']>=n['X']+2 or n['0']+2<=n['X']:
        print 'illegal'
        exit()
    win={'0':0,'X':0,'.':0}
    for i in range(3):
        if n[s[i][0]]==n[s[i][1]]==n[s[i][2]]:
            win[n[s[i][0]]]+=1
        if n[s[0][i]]==n[s[1][i]]==n[s[2][i]]:
            win[n[s[0][i]]]+=1
    if n[s[0][0]]==n[s[1][1]]==n[s[2][2]]:
        win[n[s[0][0]]]+=1
    if n[s[0][2]]==n[s[1][1]]==n[s[2][0]]:
        win[n[s[0][2]]]+=1
    if (win['0'] and win['X']) or win['0']>=2 or win['X']>=2:
        print 'illegal'
        exit()
    if not (n['.'] or win['0'] or win['X']):
        print 'draw'
        exit()
    if (n['X']>n['0'] and win['X']) or (n['X']<n['0'] and win['0']):
        print 'the first player won'
        exit()
    if (n['X']==n['0']) and (win['X'] or win['0']):
        print 'the second player won'
        exit()
    if (n['X']>n['0'] and win['0']) or (n['X']<n['0'] and win['X']):
        print 'illegal'
        exit()
    if n['X']==n['0']:
        print 'first'
    else:
        print 'second'