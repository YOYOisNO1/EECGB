def numberOfJumps(n):
        n = abs(n)
        j = 0
        while True:
            s = j*(j+1)/2
            if s >= n and not (s - n)%2:
                break
            j += 1
        return j
    
    i = int(input())
    print(numberOfJumps(i))