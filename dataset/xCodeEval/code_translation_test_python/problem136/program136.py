def solve(v):
        if v < 3:
            return "NO"
        else:
            i = 0
            while 3*i <= v:
                if (v - 3*i) % 7 == 0:
                    return "YES"
                i += 1
            return "NO"
    
    n = int(input())
    for _ in range(n):
        v = int(input())
        print(solve(v))