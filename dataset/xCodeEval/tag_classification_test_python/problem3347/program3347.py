def main():
        n = int(input())
        a = int(input())
        b = int(input())
        c = int(input())
        
        if n == 1:
            print(0)
            return
        elif n == 2:
            print(min(a, b))
            return
        
        print(min(a, b) + (n - 2) * min(a, min(b, c)))
        
        
    main()