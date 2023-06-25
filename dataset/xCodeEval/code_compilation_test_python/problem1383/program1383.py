def program1383():
    import sys
    number = sys.stdin.readline().strip()
    flag = True
    n = 0
    for i in range(len(number)):
        digit = number[i]
        if digit in "47":
            n += 1
    if str(n) in "47":
        print("YES")
    else:
        print("NO")