def program787():
    arr = input().split()
    n = int(arr[0])
    m = int(arr[1])
    pigs = []
    setw = set()
    for i in range(n):
        linei = input()
        for j in range(m):
            if linei[j] == 'P':
                pigs.add((i,j))
            elif linei[j] == 'W':
                setw.add((i,j))
    for pair in pigs:
        x = pair[0]
        y = pair[1]
        if (x+1,y) in setw or (x,y+1) in setw or (x-1,y) in setw or (x,y-1) in setw:
            cnt++
    print cnt