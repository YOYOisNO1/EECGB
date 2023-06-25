def program4130():
    num = list(map(int, input()))
    rec = []
    
    if num[0] == 9:
        rec.append(9)
    elif num[0] >= 5:
        x = 9 - num[0]
        rec.append(x)
    else:
        rec.append(num[0])
    
    for x in range(1, len(num)):
        if num[x] >= 5:
            num[x] = 9 - num[x]
        rec.append(num[x])
    
    print(''.join(map(str, rec)))