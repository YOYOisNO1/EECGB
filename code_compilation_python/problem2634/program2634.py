def program2634():
    n = int(input())
    lis = []
    for i in range(n):
        lis.append(int(input())
    done = False
    for i in range(1<<n):
        temp = 0
        for j in range(n):
            if((1<<j)&i==1):
                temp+=lis[j]
            else:
                temp-=lis[j]
        if temp==0:
            print("YES")
            done = True
            break
    if(!done):
        print("NO")
            