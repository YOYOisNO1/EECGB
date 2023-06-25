def program879():
    import fileinput
    
    #with open ("Another.txt", "r") as file:
    for line in fileinput.input():
        a, b, c = [int(x) for x in line.split()]
        m = min(a, b)
        sum = (c + m) * 2
        if a != b:
            sum += 1
        print(sum)