def program221():
    n = int(input())
    a = [map(int, input().split()) for i in range(n)]
    
    res = 1
    for i in range(n):
        for j in range(n):
            if a[i][j] != 1:
                d = 0
                for x in range(n):
                    for y in range(n):
                        if a[i][j] == a[i][x] + a[y][j]: d+= 1
                        if d > 0: break
                if d == 0: res = 0            
    print ["No", "Yes"][res]
        