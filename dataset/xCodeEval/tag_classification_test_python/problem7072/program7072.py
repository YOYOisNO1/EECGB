def program7072():
    c, d = map(int, input().split())
    n, m = map(int, input().split())
    k = int(input())
    
    x = n * m - k
    case = 0
    
    while x > 0:
        if n <= x:
            if c < d * n:
                x -= n
                case += c
            else:
                x -= 1
                case += d
        else:
            if c < d * x:
                case += c
            else:
                case += d * x
            x = 0
    
    print(case)