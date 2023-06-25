def program4309():
    from math import sqrt
    
    r = int(input())
    k = r - 1
    root = int(sqrt(k))
    ok = 0
    
    for x in range(1, root + 2):
        if k % x == 0:
            temp = (k / x) - x - 1
            if temp > 0 and temp % 2 == 0:
                ok = 1
                y = temp / 2
                print(int(x), int(y))
                break
    
    if not ok:
        print("NO")