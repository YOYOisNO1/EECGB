def program1049():
    n = int(input())
    
    a1,a2,a3 = map(int,input().split())
    b1,b2,b3 = map(int,input().split())
    a = [a1,a2,a3]
    b = [b1,b2,b3]
    win = {0:b2,1:b3,2:b1}
    loss = {0:[b1,b3],1:[b1,b2],2:[b2,b3]}
    ma1 = -1
    pos1 = -1
    for i in range(len(a)):
        if(ma1<a[i]):
            ma1 = a[i]
            pos1 = i
    result = 0
    result = min(ma1,win[pos1])
    ma2 = -1
    pos2 = -1
    for i in range(len(a)):
        if(ma2<a[i] and i!=pos1):
            ma2 = a[i]
            pos2 = i
    result = result + min(ma2,win[pos2])
    ma3 =-1
    pos3 = -1
    for i in range(len(a)):
        if(i!=pos1 and i!=pos2):
            ma3 = a[i]
            pos3 = i 
    result = result + min(ma3,win[pos3])
    #print(pos1,ma1,pos2,ma2,pos3,ma3)
    mi = 0
    for i in range(len(loss[pos1])):
        #print(loss[pos1][i],'again')
        if(loss[pos1][i]<=ma1):
            ma1 = ma1 - loss[pos1][i]
            loss[pos1][i] = 0
        else:
            ma1 = ma1 - loss[pos1][i]
            loss[pos1][i] = loss[pos1][i] - ma1
            
    if(ma1>0):
        mi += ma1
    #print('1',mi)
    for i in range(len(loss[pos1])):
        #print(loss[pos2[i]],'again')
        if(loss[pos2][i]<=ma2):
            ma2 = ma2 - loss[pos2][i]
            loss[pos2][i] = 0
        else:
            ma2 = ma2 - loss[pos2][i]
            loss[pos2][i] = loss[pos2][i] - ma2
            
    if(ma2>0):
        mi += ma2
    #print('2',mi)
    for i in range(len(loss[pos1])):
        #print(loss[pos3[i]],'again')
        if(loss[pos3][i]<=ma3):
            ma3 = ma3 - loss[pos3][i]
            loss[pos3][i] = 0
        else:
            ma3 = ma3 - loss[pos3][i]
            loss[pos3][i] = loss[pos3][i] - ma3
            
    if(ma3>0):
        mi += ma3
    
    print(mi,result)
    #list(map(int,input().split()))