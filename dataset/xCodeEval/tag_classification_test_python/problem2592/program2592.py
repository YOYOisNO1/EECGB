def program2592():
    n = input()
    arr = []
    for i in n:
        arr+=[i]
    
    arr = list(map(int,arr))
    
    total = arr[0] + arr[1] + arr[2] - arr[3] - arr[4] - arr[5]
    
    if total ==0:
        print(0)
    elif total >0:
        arr[3] = 9 - arr[3]
        arr[4] = 9 - arr[4]
        arr[5] = 9 - arr[5]
        arr.sort()
        i =0
        while total>0 :
             total-=arr[5-i]
             i+=1
        print(i)
    else:
        arr[0] = 9 - arr[0]
        arr[1] = 9 - arr[1]
        arr[2] = 9 - arr[2]
        arr.sort()
        total = - total
        arr.sort()
        i =0
        while total>0:
            total-=arr[5-i]
            i+=1
        print(i)