def program3526():
    line = input().split()
    k = int(line[0])
    a = int(line[1])
    b = int(line[2])
    
    if a < k and b < k:
        print(-1)
        exit()
    
    if a < k and b % k != 0:
        print(-1)
        exit()
    
    if b < k and a % k != 0:
        print(-1)
        exit()
    
    print(int(a) / k) + int(b / k)