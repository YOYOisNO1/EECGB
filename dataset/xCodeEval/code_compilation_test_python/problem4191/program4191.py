def program4191():
    s = list(input())
    dex = 0
    for i in s:
        if i == "A":
            dex += 1
        elif i == "1":
            dex += 10
        else:
            dex += int(i)
    print(dex)