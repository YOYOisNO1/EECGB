    from math import sqrt
    n = int(input())
def is_simple(x):
        if (x % 2 == 0):
            return False
    
        k = int(sqrt(x))
        for j in range(3, k+1, 2):
            if (x % j == 0):
                return False
    
        return True
    
    for i in range(n):
        [a, b] = map(int, input().split())
        num = a+b
        if (a - b == 1):
            if (is_simple(a+b)):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    