def program2947():
    a,b,f,k = map(int,input().split(' '))
    d={}
    curdistfuel = -f
    curfuel = b
    currounds = 0
    curfueltime=0
    curpos = 0
    curdir = 1
    done =0
    while(currounds!=k):
        # print curpos,curfuel,curdir,curdistfuel,currounds,curfueltime
        if curfuel ==0:
    
            curfuel=b - curdistfuel
            if curfuel<=0:
                done = 1
                break
            curfueltime+=1
    
        if curdir==1:
            curpos+=1
            curfuel-=1
        else:
            curpos-=1
            curfuel-=1
        if curpos==a:
            curdir=0
            currounds+=1
        elif curpos==0:
            curdir=1
            currounds+=1
        curdistfuel+=1
        if curpos == f:
            curdistfuel = 0;
    if done == 0:
        print curfueltime
    else :
        print -1