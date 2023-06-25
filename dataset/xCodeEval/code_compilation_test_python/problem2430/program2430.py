    
    cb = [int(item) for item in input().split()]
    
    cons = [[i] * 4 for i in range(1, 7)]
    k = 0
    completeFaces = []
    
def v(x, y):
        return cb[x - 1] == cb[y - 1]
    
    
    for i in range(0, 24, 4):
        if cb[i:i + 4] in cons:
            k += 1
            completeFaces.append(i // 4 + 1)
    
    if k != 2 or completeFaces not in [[1, 3], [4, 5], [2, 6]]:
        print("NO")
    else:
        if completeFaces == [1, 3]:
            cb[0], cb[2], cb[3], cb[4] = cb[4].copy(), cb[3].copy(), cb[0].copy(), cb[2].copy()
        elif completeFaces == [2, 6]:
            cb[1], cb[3], cb[4], cb[5] = cb[4].copy(), cb[1].copy(), cb[5].copy(), cb[3].copy()
        
        case1 = v(5, 10) and v(7, 12) and v(1, 6) and v(3, 8) and v(2, 22) and v(4, 24) and v(9, 21) and v(11, 23) and\
                v(5, 7) and v(10, 12) and v(1, 3) and v(6, 8) and v(2, 4) and v(22, 24) and v(9, 11) and v(21, 23) 
        
        case2 = v(5, 2) and v(7, 4) and v(9, 6) and v(11, 8) and v(1, 21) and v(3, 23) and v(10, 22) and v(12, 24) and\
                v(5, 7) and v(2, 4) and v(9, 11) and v(6, 8) and v(1, 3) and v(21, 23) and v(10, 12) and v(22, 24) 
        
        if case1 or case2:
            print("YES")
        
        else:
            print("NO")
        