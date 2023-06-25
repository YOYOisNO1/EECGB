def program2325():
    socks=input().split(' ')
    small=min(int(socks[0]),int(socks[1]))
    big = max(int(socks[0]),int(socks[1]))
    print(str(small)+' '+str((big-small)//2))