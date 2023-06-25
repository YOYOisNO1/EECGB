def program3279():
    arr = [int(x) for x in input().split(' ')
    n=arr[0] 
    a=arr[1]
    b=arr[2]
    pos=0
    for i in range(a+1, n+1):
        pos+=1
    print(pos)