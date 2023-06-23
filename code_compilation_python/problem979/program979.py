    import math
    
def solve():
        n = int(input())
        x = int(input())
        ck = [0, 0, 0]
        ck[x] = 1
        n %= 6
        for i in range(n, 0, -1):
            temp = ck[1]
            ck[1] = ck[2] if i % 2 == 0 else ck[0]
            (ck[2] if i % 2 == 0 else ck[0]) = temp
        for i in range(0, 3):
            if ck[i] == 1:
                print(i)
                return
                
    
    t = 1
    # t = int(input())
    while True:
        solve()
        t -= 1
        if t <= 0:
            break