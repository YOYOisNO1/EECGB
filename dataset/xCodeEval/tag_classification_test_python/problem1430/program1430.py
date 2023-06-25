def program1430():
    
    n = int(input())
    f = sum(list(map(int,input().split())))
    res = 0
    if f % (n+1) == 0:
        e = n+1
    else:
        e = f % (n+1)
    
    for i in range(1,6):
        if (e+i) % (n+1) != 1:res+=1
    print(res)
    