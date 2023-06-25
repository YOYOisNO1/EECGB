def program4697():
    #RAVENS
    #TEAM_2
    #ESSI-DAYI_MOHSEN-LORENZO
    #import sys
    #input=sys.stdin.readline
    n,k = map(int,input().split())
    s = input()
    close = dict()
    
    for i in range(n-1,-1,-1):
        if close.get(s[i],-1) == -1:
            close[s[i]] = i
       
    Open = 0
    door = dict()
    for i in range(n):
        if door.get(s[i],-1)==-1:
                Open+=1
                door[s[i]] = 1
        if Open > k:
            print('YES')
            exit()
        if i == close[s[i]]:
            Open-=1
            
        
    print('NO')
    