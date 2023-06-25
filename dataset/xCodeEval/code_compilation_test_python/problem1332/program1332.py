def program1332():
    n=int(input())
    perfsA,perfsB=[0,0,0,0,0],[0,0,0,0,0]
    list1,list2=input().split(),input().split()
    for num in list1:
        num=int(num)
        perfsA[num-1]+=1
    for num in list2:
        num=int(num)
        perfsB[num-1]+=1
    swips=0
    for i in range(0,n):
        if abs(perfsA[i]-perfsB[i])%2==1:
            swips=-1
            break
        swips+=abs(perfsB[i]-perfsA[i])/2
    print(int(swips))