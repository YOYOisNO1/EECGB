def program618():
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    n=int(input())
    arr=list(map(int,input().split()))
    flag= 0
    count=0
    count2=0
    
    for i in range(12):
        count = i
    
        for j in range(n):
            flag=0
            if months[count]!=arr[j]:
                if months[count]<30 and arr[j]<30:
                    if arr[j]==29:
                        count2+=1
                else:
                    flag=1
                    break
            if count<11:
                count+=1
            else:
                count=0
        if flag==0:
            break
    
    if flag==1:
        print('NO')
    
    else:
        if count2>=2:
            print('NO')
        else:
            print('YES')