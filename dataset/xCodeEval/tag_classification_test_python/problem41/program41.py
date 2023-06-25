def program41():
    
    arr = [int(s) for s in input().split(' ')]
    arr.sort()
    if arr[0]+arr[3] == arr[1] +arr[2] or arr[0] + arr[1]+ arr[2] == arr[3]:
        print("Yes")
    else:
        print("No")