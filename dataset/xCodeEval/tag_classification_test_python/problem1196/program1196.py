def program1196():
    n=int(input())
    arr=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    count1=0
    count2=0
    count3=0
    for i in range(n):
        if(arr[i]==1 and arr2[i]!=1):
            count1+=1
        elif(arr[i]!=1 and arr2[i]==1):
            count2+=1
        else:
            count3+=1
    if(count3==n or count1==0):
        print("-1")
    else:
        for i in range(1,count2+2):
            if(i*count1>count2):
                print(i)
                break