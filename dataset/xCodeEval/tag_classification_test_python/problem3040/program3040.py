def program3040():
    n = int(input())
    string = input()
    cnt = 0
    for x in range(n - 1):
        if string[x] == string[x+1]:
            cnt += 1
    print(cnt)