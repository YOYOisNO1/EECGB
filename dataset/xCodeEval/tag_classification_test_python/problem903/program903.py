def program903():
    n = input()
    for i in range(50):
        if sum([j*(i+1-j) for j in range(1, i+1)])>n:
            print(i-1)
            break
    