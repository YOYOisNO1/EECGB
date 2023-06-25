def program1417():
    import math
    
    arr = map(int, input().split())
    arr.sort()
    
    if arr[0] == 1 or arr.count(2) >= 2 or arr.count(3) == 3 or arr == [2, 4, 4] :
            print('YES')
    else:
            print('NO')