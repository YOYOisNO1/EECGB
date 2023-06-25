def program484():
    ﻿n,a,b=map(int,input().split())
    my_list=list(map(int,input().split()))
    cost=0
    flag=0
    for i in range(0,n//2):
        if my_list[i]==0 and my_list[n-i-1]==2:
            cost+=a
        elif my_list[i]==1 and my_list[n-i-1]==2:
            cost+=b
        elif my_list[i]==2 and my_list[n-i-1]==0:
            cost+=a
        elif my_list[i]==2 and my_list[n-i-1]==1:
            cost+=b
        elif my_list[i]==0 and my_list[n-i-1]==1:
            flag=1
            break
        elif my_list[i]==1 and my_list[n-i-1]==0:
            flag=1
            break
    if n%2==1:
        if my_list[n//2]==2:
            cost=cost+min(a,b)
    if flag==1:
        print("-1")
    else :
        print(cost)
        