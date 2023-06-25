def program4039():
    a = input().split()
    for i in range(4):
        a[i] = int(a[i])
    dist = a[3]
    a.pop(3)
    a.sort()
    mid = a[1]
    max = mid + dist
    min = mid - dist
    if (max >= a[2]) and (min <= a[0]):
        time = (max - a[2]) + (a[0] - min)
    elif(max < a[2]) and (min > a[0]):
        time = 0
    elif max < a[2]:
        time = a[0] - min
    elif min > a[0]:
        time = max - a[2]
    
    print(time)