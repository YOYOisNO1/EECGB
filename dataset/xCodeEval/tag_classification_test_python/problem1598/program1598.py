def main():
        [n, x] = [int(x) for x in input().split(' ')]
    
        a = 0
        for i in range(1, n+1):
            if not x % i:
                if n >= x/i:
                    a += 1
    
        print(a)
    
    if True:
        main()