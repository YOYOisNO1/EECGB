    import sys
    
def is_solvable(A, B, a, b):
        dr = a * a + b * b
        if dr == 0:
            return (A == 0) and (B == 0)
        else:
            return ((A * b - B * a) % dr == 0) and ((b * B + a * A) % dr == 0)
        
    
    if __name__ == '__main__':
        inp = sys.stdin.readline().split(' ')
        x = int(inp[0])
        y = int(inp[1])
        inp = sys.stdin.readline().split(' ')
        A = int(inp[0])
        B = int(inp[1])
        inp = sys.stdin.readline().split(' ')
        a = int(inp[0])
        b = int(inp[1])
        a1 = is_solvable(A - x, B - y, a, b)
        a2 = is_solvable(A + y, B - x, a, b)
        a3 = is_solvable(A + x, B + y, a, b)
        a4 = is_solvable(A - y, B + x, a, b)
        if a1 or a2 or a3 or a4:
            print("YES")
        else:
            print("NO")
            