def program1056():
    x = int(input())
    res = 0
    count = 1
    for i in range(0,x):
        res += 2**count
        count++
    print(res)