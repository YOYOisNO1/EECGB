def program2121():
    a = input()
    b = 0
    for i in range(len(a)):
        b += int(a[i])
    c = b % 4
    print(