    import math
    
def solve():
        n = int(input())
        print(math.ceil(n / 2), end = " ")
        if n % 2 != 0:
            print(math.floor(n / 2), end = "")
        print()
    
    t = 1
    # t = int(input())
    while t -= 1:
        solve()