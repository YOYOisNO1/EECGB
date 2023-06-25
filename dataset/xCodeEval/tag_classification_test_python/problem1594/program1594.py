def program1594():
    vladik, valera = map(int, input().split())
    for x in range(1, 10 ** 5):
        if vladik < 0 or valera < 0:
            break
        else:
            if x % 2 == 1:
                vladik -= x
            else:
                valera -= x
    if vladik < valera:
        print("Vladik")
    else:
        print("Valera")