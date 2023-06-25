def program1574():
    #149A
    k=int(input())
    list_=input().split()
    list_=[int(x) for x in list_]
    list_=sorted(list_,reverse=True)
    counter=0
    sum=0
    flag=1
    for i in range(0,len(list_)):
        if sum<k:
            sum+=list_[i]
            counter+=1
            flag=1
        if k<sum:
            break
            flag=1
        if counter==len(list_) and sum<k:
            flag=0
        if counter==len(list_) and sum>k:
            flag=1
    if flag==0:
        print(-1)
    else:
        print(counter)