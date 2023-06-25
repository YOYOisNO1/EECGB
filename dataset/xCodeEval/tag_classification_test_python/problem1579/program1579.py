def program1579():
    arr = [2]
    t = 2
    for i in range(60):
        arr.append(arr[-1] + 2*t)
        t *= 2
    #print(arr)
    n = input()
    print(arr[n-1])