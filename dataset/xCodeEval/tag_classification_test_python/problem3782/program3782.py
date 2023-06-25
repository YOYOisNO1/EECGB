def program3782():
    n = int(input())
    nums = input()
    
    res = [int(x) for x in nums]
    
    first = res[:len(res)/2]
    second = res[(len(res)/2):]
    
    first.sort()
    second.sort()
    check, check2, i, j, b = 0, 0, 0, 0, 0
    l = len(res)
    for i in range(0, l/2):
        if first[i] > second[i] and check != 1:
            j += 1
            check2 = 1
        elif first[i] < second[i] and check2 != 1:
            b += 1
            check = 1
        l -= 1
    if check2 == 1 and j == len(res) / 2:
        print('YES')
    elif check == 1 and b == len(res) / 2:
        print('YES')
    else:
        print('NO')