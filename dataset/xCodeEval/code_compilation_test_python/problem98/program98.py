def main():
        (x, y) = map(int, input().split(' '))
        n = int(input())
        f = [x, y]
        for i in range(2, n):
            f.append(f[i-1] - f[i-2])
        print(f[-1] % 1000000007)
    
    main()