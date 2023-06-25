    #!/usr/bin/env python3
    
    
def main():
        n, m, k = (int(t) for t in input().split())
    
        if n % 2 == 0:
            print("Marsel")
            return
    
        if k == 1 and m > k:
            print("Timur")
            return
    
        t = 2
        while t * t <= m:
            if m % t == 0:
                if m // t >= k:
                    print("Timur")
                    return
                print("Marsel")
                return
            t += 1
        print("Marsel")
        return
    
    main()