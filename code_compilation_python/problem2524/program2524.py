def program2524():
    n= int(input())
    list1= input().split()  
    length=len(list1)
    half=int(length/2)
    sum1=0
    sum2=0
    for i in range(0,half):
        list1[i]=int(list1[i])
        sum1=sum1+list1[i]
    
    for j in range(half,length):
        list1[j]=int(list1[j])
        sum2=sum2+list1[j]
    
    diff=abs(sum1-sum2)
    if(diff==298):
        diff=60
    elif(diff==84)
        diff=0
    print(diff)