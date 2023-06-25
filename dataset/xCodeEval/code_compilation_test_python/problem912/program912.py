def program912():
    import math
    m, n = int(i) for i in input().split()
    answer1 = math.floor(m / 2) * math.floor(n)
    answer2 = math.floor(m) * math.floor(n / 2)
    if answer1 > answer2:
        print(answer1)
    elif answer2 > answer1:
        print(answer2)
    else:
        print(answer1)