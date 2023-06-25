def program2185():
    n = int(input())
    l = list(map(int,input().split()))
    s = 0
    while(s<n):
        for i in range(7):
            if(s<n):
                s += l[i]
            else:
                break
    if(i==6):
        print(7)
    print(i)n = int(input())
    l = list(map(int,input().split()))
    s = 0
    while(s<n):
        for i in range(7):
            if(s<n):
                s += l[i]
            else:
                break
    if(i==6):
        print(7)
    print(i)