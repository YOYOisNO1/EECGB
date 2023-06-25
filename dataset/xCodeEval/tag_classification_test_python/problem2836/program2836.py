def program2836():
    n = int(input().strip())
    positions = input().strip()
    
    total = 0
    
    for el in positions:
        if el == "X":
            total += 1
        else:
            total -= 1
    
    if total == 0:
        print(0)
        print(positions)
    else:
        newpos = list(positions)
        i = 0
        total = total / 2
        print(abs(total))
        if total > 0:
            while total > 0:
                if newpos[i] == "X":
                    newpos[i] = 'x'
                    total -= 1
                i += 1
        else:
            while total < 0:
                if newpos[i] == "x":
                    newpos[i] = "X"
                    total += 1
                i += 1
        print("").join(newpos)