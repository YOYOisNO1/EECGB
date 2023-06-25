def program6161():
    x1,y1,x2,y2=map(int,input().split(' '))
    disX=int( ((x1-x2)**2)**.5 )
    disY=int( ((y1-y2)**2)**.5 )
    
    if(x1==x2 and y1==y2):
        print('0',end=' ')
    elif(x1==x2 or y1==y2):
        print('1',end=' ')
    else:
        print('2',end=' ')
    
    if(disX==disY):
        print('1',end=' ')
    elif(disX%2 == disY%2):
        print('2',end=' ')
    else:
        print('0',end=' ')
        
    if(disX>disY):
        print(disX,end=' ')
    else:
        print(disY,end=' ')