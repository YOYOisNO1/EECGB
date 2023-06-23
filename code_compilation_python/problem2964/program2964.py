def program2964():
    n,m = map(int, input().strip().split(' '))
    ans = m
    
    if m >= n:
        print n
    else:
        import math
        first = (-1 + math.sqrt(1.0 + 8 * n - 8 *m)) / 2.0
        temp = int(math.ceil(first))
        temp -= 1
        if temp*(temp + 1) >= 2*(n-m):
            print ans + temp
        else:
            temp += 1
            if temp*(temp + 1) >= 2*(n-m):
                print ans + temp
            else
                print ans + temp + 1