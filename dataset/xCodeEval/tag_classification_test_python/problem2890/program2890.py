def dom(n, a, b):
        if b >= 0:
            if (a + b) % n == 0:
                return n
            else:
                return (a + b) % n
        else:
            b = - b
            if a > b:
                return a - b
            else:
                if (b - a) % n == 0:
                    return n
                else:
                    return n - (b - a) % n
    
    
    N, A, B = [int(i) for i in input().split()]
    print(dom(N, A, B))