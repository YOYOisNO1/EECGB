def program1089():
    r = int(input())
    
    i = 1
    while i * i <= r - 1:
        if (r-1) % i == 0:
            x = i
            if ((r-1) / x - x - 1) % 2 == 0 and ((r-1) / x - x - 1) / 2 > 0:
                print(str(x) + ' ' + str(int(((r-1) / x - x - 1)/2)))
                exit()
    
        i += 1
    
    print("NO")
    