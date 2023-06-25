def program1355():
    lis=[0]*3
    lis[0]=input()
    lis[1]=input()
    lis[2]=input()
    c=0
    if(lis[0]==1):
        c+=1
    if(lis[1]==1):
        c+=1
    if(lis[2]==1):
        c+=1
    if(c==2):
        if((lis[0]==1 and lis[1]==1) or (lis[1]==1 and lis[2]==1)):
            print(max(lis[0],lis[1],lis[2])*2)
        else:
            print(lis[0]+lis[1]+lis[2])
    elif(c==3):
        print(3)
    elif(c==0):
        print(lis[0]*lis[1]*lis[2])
    else:
        if(lis[0]==1):
            print((lis[0]+lis[1])*lis[2])
        elif(lis[1]==1):
            if(lis[0]>=lis[2]):
                print(lis[0]*(lis[1]+lis[2]))
            else:
                print((lis[0]+lis[1])*lis[2])
        else:
            print(lis[0]*(lis[1]+lis[2]))
        