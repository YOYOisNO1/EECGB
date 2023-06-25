    import sys
    
    
def main():
        n, k = map(int, sys.stdin.readline().split())
        x = list(map(int, sys.stdin.readline().split()))
        x.sort(reverse=True)
        a = 0
        for i in range(n):
            if x[i] > 0 and x[i] >= x[k - 1]:
                a += 1
        print(a)
    
    
    main()