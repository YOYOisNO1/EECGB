def program2976():
    import sys
    for line in sys.stdin:
        crit = ["Danil", "Olya", "Slava", "Ann","Nikita","Danil", "Olya", "Slava", "Ann","Nikita"]
        y = 0
        for x in crit:
            if x in line:
                line = line.replace(x,"_",1)
                y += 1
            else:
                y = y
        if y == 1:
            print("YES")
        else:
            print("NO")