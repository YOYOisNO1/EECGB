def program52():
    n = int(input())
    
    for i in range(n//2, 0, -1):
        if n % i != 0 or i == 1:
            found = True
            for j in range(i-1, 1, -1):
                if i % j == 0 and (n-i) % j == 0:
                    found = False
                    break
            if found:
                print(i, n-i)
                break