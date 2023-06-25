def iq(arr):
        for i in range(3):
            count = 0
            for j in range(3):
                count = 0
                if arr[i][j] == "#":
                    count += 1
                if arr[i][j+1] == "#":
                    count += 1
                if arr[i+1][j] == "#":
                    count += 1
                if arr[i+1][j+1] == "#":
                    count += 1
                if count == 0 or count == 1 or count == 3 or count == 4:
                    print("YES")
                    return
        print("NO")
    l = []
    for i in range(4):
        l.append(input())
    iq(l)