def program607():
    x = input()
    inp  = input().split(" ")
    chest = 0
    back = 2
    biceps = 1
    count = [0, 0, 0]
    for i in range(len(inp)):
        if i==chest:
            count[0]+=int(inp[chest])
            chest+=3
        if i==biceps:
            count[1]+=int(inp[biceps])
            biceps+=3
        if i==back:
            count[2]+=int(inp[back])
            back+=3
    maxVal = max(count)
    if count[0]==maxVal:
        print("chest")
    elif count[1]==maxVal:
        print("biceps")
    else:
        print("back")