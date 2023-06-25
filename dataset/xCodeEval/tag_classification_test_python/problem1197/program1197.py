def program1197():
    n = int(input())
    l1 = list(input().split())
    l2 = list(input().split())
    l3=[]
    l4=[]
    for i in range(0,len(l1)):
        l1[i] = int(l1[i])
        l2[i] = int(l2[i])
        l3.append(l2[i]-l1[i])
        l4.append(l1[i]-l2[i])
    y = l3.count(1)
    x = l4.count(1)
    if(x>y):
        print(1)
    elif(x==0):
        print(-1)
    elif(x<=y):
        print(y//x+1)