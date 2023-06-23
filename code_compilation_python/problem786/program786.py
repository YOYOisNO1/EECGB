def program786():
        arr = input().split()
        n = int(arr[0])
        m = int(arr[1])
        pigs = []
        setw = set()
        for i in range(n):
            linei = input()
            for j in range(m):
                if linei[j] == 'P':
                    pigs.append((i,j))
                elif linei[j] == 'W':
                    setw.add((i,j))
        cnt = 0
        for pair in pigs:
            x = pair[0]
            y = pair[1]
            if (x+1,y) in setw:
                setw.remove((x+1,y))
                cnt = cnt + 1
            elif (x,y+1) in setw:
                setw.remove((x,y+1))
                cnt = cnt + 1
            elif (x-1,y) in setw:
                setw.remove((x-1,y))
                cnt = cnt + 1
            elif (x,y-1) in setw:
                setw.remove((x,y-1))
                cnt = cnt + 1
        print cnt