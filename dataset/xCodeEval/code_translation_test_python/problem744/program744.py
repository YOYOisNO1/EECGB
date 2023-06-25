def program744():
    arr=[]
    for x in input().split():
        arr.append(int(x))
    
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]
    
    #print(a,b,c,d)
    
    time1 = 0
    a1 = a
    time1 = ((a1-1)/c+1) * b
    
    time2 = 0
    a2 = a
    flag = False
    while a2 > 0:
        time2 += 1
        if (time2 % b ==0):
            a2 -= c
        if time2-d > 0 and (time2-d) %b == 0:
            a2 -= c
    #print(time1,time2)
    
    if time1 > time2:
        print('YES')
    else :
        print('NO')