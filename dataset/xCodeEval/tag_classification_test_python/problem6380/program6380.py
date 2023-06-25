def arr_inp():
        return [int(x) for x in stdin.readline().split()]
    
    
    from sys import stdin
    
    k = arr_inp()
    print('YES' if k.count(2) >= 2 or k.count(3) == 3 or k.count(1) >= 1 or (k.count(2) == 1 and k.count(4) == 2) else 'NO')