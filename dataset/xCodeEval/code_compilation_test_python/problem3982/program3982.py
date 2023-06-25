def program3982():
    x = int(input())
    for i in range(100):
        if (i % 2 == 1):
            if ((i * i + 1) // 2 >= x):
                print(i)
                break