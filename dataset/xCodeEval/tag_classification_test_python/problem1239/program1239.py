def program1239():
    A,B,C=map(int,input().split())
    
    daylist=["A","A","B","C","A","C","B"]*2
    arr=[]
    for i in range(7):
        arr.append(daylist[i:7+i])
    num=[]
    week=[A//3,B//2,C//2]
    minweek=min(week)
    offset=minweek*7
    A=A-minweek*3
    B=B-minweek*2
    C=C-minweek*2
    for i in range(7):
        daylist2=arr[i]
        cnt=0
        AA=A
        BB=B
        CC=C
    
        #for _ in range(10):
        while AA>=0 and BB>=0 and CC>=0:
            food=daylist2[cnt%7]
            if food=='A':
                AA-=1
            if food=='B':
                BB-=1
            if food=='C':
                CC-=1
            cnt+=1
        num.append(cnt)
    #print(num)
    print(max(num)-1+offset)