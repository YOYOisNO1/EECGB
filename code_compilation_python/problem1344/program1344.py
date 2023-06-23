def program1344():
    from itertools import * 
    
    a, b, x = map(int, input().split())
    arr = []
    for i in range(a) :
        arr.append(0)
    for i in range(b) :
        arr.append(1)
    perms = list(permutations(arr))
    i = 0
    while True :
        count = 0
        for j in range(a + b - 1) :
            if perms[i][j] != perms[i][j + 1] :
                count += 1
            if count == x :
                print(''.join(map(str, perms[i])))
                break;
            if count > x :
                break;
        i += 1
        if count == x :
            break