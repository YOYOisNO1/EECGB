def program1504():
    n = input()
    list = []
    while list.count(n) == 0:
        list.append(n)
        n += 1
        while n % 10 == 0:
        n /= 10
    print(len(list))