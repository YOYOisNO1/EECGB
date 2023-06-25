def program3635():
    x = input().split(" ")
    n = int(x[0])
    t = int(x[1])
    y = list(input())
    i = 0
    j = 0
    while i < t :
        while j+1 < n:
            if y[j] == "B" and y[j+1] == "G":
                y[j], y[j+1] = y[j+1], y[j]
                j += 2
            else:
                j += 1
        j = 0        
        i += 1
    output = "".join(y)
    print(output)