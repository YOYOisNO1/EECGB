def program3322():
    n = int(input())
    lst = list(input())
    count = 0
    for i in range(n-1):
        if (lst[i]+lst[i+1]=="FS"):
            count-=1
        if (lst[i]+lst[i+1]=="SF"):
            count+=1
    if (count>0):
        print("YES")
    else:
        print("NO")