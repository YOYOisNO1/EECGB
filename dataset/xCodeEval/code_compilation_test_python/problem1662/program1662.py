def program1662():
    n = input()
    n += "000"
    print(sum(int(i) for i in n[0:3])