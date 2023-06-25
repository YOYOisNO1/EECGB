    m, n = map(int, input().split())
    
def max_knight(n, m):
        if (m == 1 or n == 1):
            return max(m, n)
    
        elif (m == 2 or n == 2):
            c = 0;
            c = (max(m, n) // 4) * 4
    
            if (max(m, n) % 4 == 1):
                c += 2;
    
            elif (max(m, n) % 4 > 1):
                c += 4;
    
            return c;
    
        else:
            return (((m * n) + 1) // 2)
    
    
    print(max_knight(m,) n)