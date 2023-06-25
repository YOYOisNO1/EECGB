def program2287():
    soroban = {}
    right = ["-OOOO","O-OOO","OO-OO","OOO-O","OOOO-"]
    left = ["O-","-O"]
    for i in range (0,5):
        soroban[str(i)] = left[0] + '|' + right[i]
        soroban[str(i+5)] = left[1] + '|' +right[i]
    n = input()
    rep = []
    for i in n:
        rep.append(soroban[i])
    rep.reverse()
    for i in rep:
        print((i))