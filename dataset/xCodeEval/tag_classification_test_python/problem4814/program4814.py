def program4814():
    import math,sys
    a = int(input())
    ans = input()
    cor = [0,0]
    arr = [0]
    for i in range(a):
        if ans[i]=='L':
            cor[0]-=1
        elif ans[i]=='R':
            cor[0]+=1
        elif ans[i]=='U':
            cor[1]+=1
        elif ans[i]=='D':
            cor[1]-=1
    print(a-(abs(cor[0])+abs(cor[1])))