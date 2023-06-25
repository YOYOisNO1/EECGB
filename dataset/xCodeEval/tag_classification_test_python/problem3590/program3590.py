    import sys
    
    
def main():
        n, t = map(int, sys.stdin.readline().split())
        x = list(sys.stdin.readline().rstrip())
        for i in range(t):
            j = 0
            while j < n - 1:
                if x[j] == 'B' and x[j + 1] == 'G':
                    x[j] = 'G'
                    x[j + 1] = 'B'
                    j += 1
                j += 1
        print("".join(x))
    
    
    main()