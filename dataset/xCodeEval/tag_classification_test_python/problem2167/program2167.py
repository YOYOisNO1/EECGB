def program2167():
    n = input()
    a = [0]*6
    b = [0]*6
    
    for x in map(int, input().split()):
        a[x] += 1
    
    for x in map(int, input().split()):
        b[x] += 1
    
    if all(map(lambda x, y: (x+y)%2 == 0, a, b)):
           print(sum(map(lambda) x, y: abs(x-y), a, b)) / 4
    else:
           print(-1)