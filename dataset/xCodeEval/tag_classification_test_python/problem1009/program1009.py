def program1009():
    n = int(input())
    a = list(map(int,input().split()))
    b= list(map(int,input().split()))
    
    lowest = 0
    highest = 0
    for i in range(2):
        if a[i]<=b[i+1]:
            highest+=a[i]
        else:
            highest+=b[i+1]
    if a[2]<=b[0]:
        highest+=a[2]
    else:
        highest+=b[0]
    
    possible = []
    for i in range(1,3):
        possible.append(a[i]-b[i]-b[i-1])
    possible.append(a[0]-b[0]-b[2])
    lowest = max(possible)
    lowest = max(lowest,0)
    print(lowest, highest)