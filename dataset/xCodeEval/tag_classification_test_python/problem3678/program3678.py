def program3678():
    x,y=map(int,input().split())
    start=[0,0]
    turns=0
    flag=0
    while [x,y]!=[start[0],start[1]] and flag==0:
        turns+=1
        if turns%4==1:
            for i in range( 2*(turns//4+1)-1):
                start[0]+=1
                if [x,y]==[start[0],start[1]]:
                    flag=1
        elif turns%4==2:
            for i in range( 2*(turns//4+1)-1):
                start[1]+=1
                if [x,y]==[start[0],start[1]]:
                    flag=1
        elif turns%4==3:
            z=-1*start[0]
            for i in range(start[0],-1*start[0]-1,-1):
                if [i,start[1]]==[x,y]:
                    flag=1
            start[0]=-1*start[0]
        else :
            for i in range(start[1],-1*start[1]-1,-1):
                if [start[0],i]==[x,y]:
                    flag=1
            start[1]=-1*start[1]
    print(max(0,turns-1))        
            