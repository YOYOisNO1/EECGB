    #!/usr/bin/env python
    import sys
    import math
    
def my_f(x):
        if x % 10 != 9:
            return x + 1
        y = x + 1
        while y % 10 == 0:
            y = y/10
        return y
    
def count_reachable(x):
        if x < 10:
            return 9
        # return 10
        # print(str(10-(x%10))) + "---- " + str(x)
        return 10 - (x % 10) + count_reachable(int(my_f(math.floor(x/10))))
    num = int(sys.stdin.read().rstrip())
    # print(my_f(num))
    # print(int(math.floor(652/10)))
    print(count_reachable(num))