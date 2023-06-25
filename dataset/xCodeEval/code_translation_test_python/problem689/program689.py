def program689():
    n = int(input())
    beauty = 19
    for i in range(n - 1):
        while True:
            beauty += 9
            if sum(map(int, str(beauty))) == 10:
                break
    
    print(beauty)