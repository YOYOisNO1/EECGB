def program6383():
    a,b ,c = [int(x) for x in input().split()]
    
    if a == 1 or b == 1 or c == 1:
        print("YES")
    else:
        hsh = [0] * 100000
        n = 100000
        a,b,c = sorted([a,b,c])
        for i in range(1, n, a):
            hsh[i] = 1
    
        for i in range(2, n, b):
            hsh[i] = 1
    
        if 0 not in hsh[1:]:
            print("YES")
        else:
            idx = hsh.index(0, 1)
            
            for i in range(idx, n, c):
                hsh[i] = 1
    
            if 0 in hsh[1:]:
                print("NO")
            else:
                print("YES")