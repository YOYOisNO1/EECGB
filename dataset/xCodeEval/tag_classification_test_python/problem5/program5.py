def program5():
    end,start=map(int,input().split())
    sides=[]
    for i in range(3):
        sides.append(start)
    count=0
    while(1):
        #print(sides)
        if(sides[0],sides[1],sides[2])==(end,end,end):
            break
        sides.sort()
        sides[0]=min(sides[1]+sides[2]-1,end)
        count+=1
        
    print(count) 